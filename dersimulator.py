from source.Processing import measurements
from source.Processing import structures
from source.LoadFlow import powerflow
from source.Processing import dictionaries

################################################################################
import shutil
import json
import os


############################# Initializing Results filesystem ##################

if not os.path.exists("Results/"):
    os.makedirs("Results/")


############################## Get circuit elements ############################

(FEEDERs, LOADs, PVs, DERs) = dictionaries.get_nodal_elements()

(PVs, DERs) = dictionaries.get_ders_elements(PVs, DERs)

(LOADs) = dictionaries.get_nodal_loads(LOADs)


############################## Power flow block ################################
for feeder in FEEDERs:
    Circuit = powerflow.run(feeder, LOADs, PVs, DERs)

    # Define structures
    bus = structures.bus(Circuit)
    elements = structures.elements(Circuit)

for feeder in FEEDERs:
    ############################## Get measures ################################
    bus = measurements.json_busdata(Circuit, bus, Circuit.AllBusNames)
    elements = measurements.json_elementsdata(Circuit, elements, Circuit.AllElementNames)

    print("Breakpoint")

    # Save files
    with open(f"Results/{feeder}_bus.json", "w") as f:
        json.dump(bus, f, indent=2)

    with open(f"Results/{feeder}_elements.json", "w") as f:
        json.dump(elements, f, indent=2)

    print("Breakpoint")
