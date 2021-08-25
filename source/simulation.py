from source.Processing import measurements
from source.Processing import structures
from source.LoadFlow import powerflow
import pandas as pd
import json


def save_jsonfiles(feeder, bus, elements):
    ############################ Save files ####################################
    with open(f"Results/{feeder}_bus.json", "w") as f:
        json.dump(bus, f, indent=2)

    with open(f"Results/{feeder}_elements.json", "w") as f:
        json.dump(elements, f, indent=2)
    return


def save_csvfiles(feeder, bus, elements):
    bus.to_csv(f"Results/{feeder}_bus.csv")
    elements.to_csv(f"Results/{feeder}_elements.csv")
    return


def get_resultlists(config, feeder, Circuit):
    if config["Results"]["Bus"] in ["All", "all"]:
        bus_list = Circuit.AllBusNames
    else:
        RESULT = json.load(open(config["Results"]["Bus"]))
        bus_list = RESULT[feeder]["Bus"]
    if config["Results"]["Elements"] in ["All", "all"]:
        elements_list = Circuit.AllElementNames
    else:
        RESULT = json.load(open(config["Results"]["Elements"]))
        elements_list = RESULT[feeder]["Elements"]
    return bus_list, elements_list


def snapshot(config, feeder, LOADs, PVs, DERs):
    print("Running snapshot powerflow")
    Circuit = powerflow.run(feeder, LOADs, PVs, DERs)

    if config["Simulation"]["Output format"] == "json":
        (bus_list, elements_list) = get_resultlists(config, feeder, Circuit)
        ######################## Define structures #############################
        bus = structures.json_bus(bus_list)
        elements = structures.json_elements(elements_list)
        ######################## Get measures ##################################
        bus = measurements.json_busdata(Circuit, bus, bus_list)
        elements = measurements.json_elementsdata(Circuit, elements, elements_list)
        save_jsonfiles(feeder, bus, elements)

    elif config["Simulation"]["Output format"] == "dataframe":
        (bus_list, elements_list) = get_resultlists(config, feeder, Circuit)
        bus = measurements.dataframe_busdata(Circuit, bus_list)
        elements = measurements.dataframe_elementsdata(Circuit, elements_list)
        save_csvfiles(feeder, bus, elements)
    return


def time_series(feeder, bus, elements, counter, LOADs, PVs, DERs):
    print(f"executing the load flow number {counter+1} for the feeder {feeder}")
    config = json.load(open("config.json"))
    Circuit = powerflow.run(feeder, LOADs, PVs, DERs)
    (bus_list, elements_list) = get_resultlists(config, feeder, Circuit)
    if counter == 0:
        ######################## Define structures #############################
        bus = structures.json_bus(bus_list)
        elements = structures.json_elements(elements_list)
    bus = measurements.json_busdata(Circuit, bus, bus_list)
    elements = measurements.json_elementsdata(Circuit, elements, elements_list)

    return bus, elements
