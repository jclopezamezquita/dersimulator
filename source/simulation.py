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


def snapshot(config, feeder, LOADs, PVs, DERs):
    print("Running snapshot powerflow")
    Circuit = powerflow.run(feeder, LOADs, PVs, DERs)

    if config["Simulation"]["Output format"] == "json":
        ######################## Define structures #############################
        bus = structures.json_bus(Circuit)
        elements = structures.json_elements(Circuit)
        ######################## Get measures ##################################
        bus = measurements.json_busdata(Circuit, bus, Circuit.AllBusNames)
        elements = measurements.json_elementsdata(
            Circuit, elements, Circuit.AllElementNames
        )
        save_jsonfiles(feeder, bus, elements)

    elif config["Simulation"]["Output format"] == "dataframe":
        bus = measurements.dataframe_busdata(Circuit, Circuit.AllBusNames)
        elements = measurements.dataframe_elementsdata(Circuit, Circuit.AllElementNames)
        save_csvfiles(feeder, bus, elements)
        a = 1
    return


def time_series():
    print("Running time-series powerflow")
