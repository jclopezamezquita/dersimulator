from source.Processing import dictionaries
from source.Tools import plot
from datetime import datetime
from dateutil import parser
from source import simulation
import shutil
import json
import sys
import os


############################# Initializing Results filesystem ##################
if not os.path.exists("Results/"):
    os.makedirs("Results/")

############################## Get circuit elements ############################
(FEEDERs, LOADs, PVs, DERs) = dictionaries.get_nodal_elements()
(PVs, DERs) = dictionaries.get_ders_elements(PVs, DERs)
(LOADs) = dictionaries.get_nodal_loads(LOADs)

############################## Get simulation atributes ########################
config = json.load(open("config.json"))

############################## Get DERs operation ##############################
if config["DERs"]["Operation"] != "None":
    DERs_operation = json.load(open(config["DERs"]["Operation"]))

############################## Snapshott powerflow #############################
if config["Simulation"]["Type"] == "snapshot":
    print("Snapshot simulation")
    ########################## run snapshot powerflow ##########################
    for feeder in FEEDERs:
        simulation.snapshot(config, feeder, LOADs, PVs, DERs)


############################## Time-series powerflow ###########################
elif config["Simulation"]["Type"] == "time-series":
    if config["Simulation"]["Output format"] != "json":
        print(f"Only json format is supported for time-series simulation")
        sys.exit(0)
    if config["Simulation"]["Datetime"] == "Now":
        date = datetime.now()
    try:
        date = parser.parse(config["Simulation"]["Datetime"])
    except:
        print("Date out of iso format")
        sys.exit(0)
    timestep = config["Simulation"]["Time step"]
    for feeder in FEEDERs:
        for counter in range(0, config["Simulation"]["Samples"]):
            if counter == 0:
                (bus, elements) = (dict(), dict())
            if config["DSS"]["PVs curves"] != "None":
                PVCURVES = json.load(open(config["DSS"]["PVs curves"]))
            if config["DSS"]["Loads curves"] != "None":
                LOADCURVES = json.load(open(config["DSS"]["Loads curves"]))

            for pv in PVs[feeder]:
                PVs[feeder][pv]["mul"] = PVCURVES[feeder][
                    PVs[feeder][pv]["DailyCurve"]
                ][counter]
            for load in LOADs[feeder]:
                LOADs[feeder][load]["mul"] = LOADCURVES[feeder][
                    LOADs[feeder][load]["DailyCurve"]
                ][counter]
            for der in DERs[feeder]:
                DERs[feeder][der]["CSmul"] = (
                    DERs_operation[der]["enabled"][counter]
                    * DERs_operation[der]["operation"][counter]
                    * DERs_operation[der]["smart_charging"][counter]
                )
            (bus, elements) = simulation.time_series(
                feeder, bus, elements, counter, LOADs, PVs, DERs
            )
            bus["time-step"].append(date.isoformat())
            elements["time-step"].append(date.isoformat())
        simulation.save_jsonfiles(feeder, bus, elements)
        plot.result_bus(config, date, feeder)
        plot.result_elements(config, date, feeder)

else:
    print("This type of simulation is not supported")
    sys.exit(0)


print("End of simulation")
sys.exit(0)
