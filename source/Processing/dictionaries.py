import json
import os


def get_nodal_elements():
    ######################### Load config files ################################
    config = json.load(open("config.json"))
    FEEDERs = config["DSS"]["feeders"]

    ######################### Create Simulation Dictionaries ###################
    LOADs = {}  # Create empty dictionary for loads
    PVs = {}  # Create empty dictionary for PV systems
    DERs = {}  # Create empty dictionary for DERs set

    for feeder in FEEDERs:
        LOADs.update({feeder: {}})
        PVs.update({feeder: {}})
        DERs.update({feeder: {}})

    return FEEDERs, LOADs, PVs, DERs


def get_nodal_loads(LOADs):
    ######################### Load config files ################################
    config = json.load(open("config.json"))
    FEEDERs = config["DSS"]["feeders"]
    for feeder in FEEDERs:
        if config["DSS"]["Loads file name"] != "None":
            file = config["DSS"]["Loads file name"]
            path = f'{config["DSS"]["PATH"]}/{feeder}'
            DEVICES = json.load(open(f"{path}/{file}"))
            for device in DEVICES:
                LOADs[feeder].update({device: DEVICES[device]})
                LOADs[feeder][device].update({"mul": 1})
    return LOADs


def get_ders_elements(PVs, DERs):
    ######################### Load config files ################################
    config = json.load(open("config.json"))
    FEEDERs = config["DSS"]["feeders"]

    for feeder in FEEDERs:
        ##################### Read DERs data ###################################
        if config["DERs"]["Scenario"] != "None":
            DEVICES = json.load(open(config["DERs"]["Scenario"]))
            for device in DEVICES:
                if DEVICES[device]["feeder"] == feeder:
                    if DEVICES[device]["type"] == "PV":
                        PVs[feeder].update({device: DEVICES[device]})
                        PVs[feeder][device].update({"mul": 1})
                    else:
                        DERs[feeder].update({device: DEVICES[device]})
                        DERs[feeder][device].update({"CSmul": 1})
                        DERs[feeder][device].update({"PVmul": 1})
                        DERs[feeder][device].update({"BESSmul": 1})
        if config["DSS"]["PVs file name"] != "None":
            file = config["DSS"]["PVs file name"]
            path = f'{config["DSS"]["PATH"]}/{feeder}'
            DEVICES = json.load(open(f"{path}/{file}"))
            for device in DEVICES:
                PVs[feeder].update({device: DEVICES[device]})
                PVs[feeder][device].update({"mul": 1})

    return PVs, DERs
