from dss import DSS
import numpy as np
import os.path
import json
import math
import sys


config = json.load(open("config.json"))
PATH = config["DSS"]["PATH"]

LIST = {
    'Load': ['Bus1', 'Phases', 'kV', 'kW', 'pf', 'vminpu'],
    'PVs': ['Bus1', 'Phases', 'kV', 'kW', 'pf', 'Conn', 'Model', 'Enabled']
}

def run(feeder, LOADs, PVs, DERs):
    # Start openDSS
    DSS.Start(0)

    # Get references to the main classes to make code shorter
    Text = DSS.Text
    Circuit = DSS.ActiveCircuit
    Solution = DSS.ActiveCircuit.Solution

    # Initilize matplot
    DSS.ClearAll()
    Text.Command = f"Redirect {PATH}/{feeder}/Master.dss"

    for load in LOADs[feeder]:
        newload = f'New load.{load}'
        for key in LOADs[feeder][load]:
            if key in LIST['Load']:
                # Add condition for kW
                newload = newload + f' {key}={LOADs[feeder][load][key]}'
        Text.Command = newload

    for pv in PVs[feeder]:
        newpv = f'New load.{pv}'
        for key in PVs[feeder][pv]:
            if key in LIST['PVs']:
                newpv = newpv + f' {key}={PVs[feeder][pv][key]}'
        Text.Command = newpv

    for der in DERs[feeder]:
        if "CS" in DERs[feeder][der]["type"]:
            Text.Command = f"New Load.{der}_CS Bus1={DERs[feeder][der]['node']} \
                Phases={DERs[feeder][der]['phases']} kV={DERs[feeder][der]['kV']} \
                kW={DERs[feeder][der]['kW_CS']} PF={DERs[feeder][der]['pf']}"

        if "PV" in DERs[feeder][der]["type"]:
            Text.Command = f"New Load.{der}_PV Bus1={DERs[feeder][der]['node']}\
                Phases={DERs[feeder][der]['phases']} kV={DERs[feeder][der]['kV']} \
                kW={DERs[feeder][der]['kW_PV']} PF={DERs[feeder][der]['pf']}"

        if "BESS" in DERs[feeder][der]["type"]:
            Text.Command = f"New Load.{der}_BESS Bus1={DERs[feeder][der]['node']}\
                Phases={DERs[feeder][der]['phases']} kV={DERs[feeder][der]['kV']} \
                kW={DERs[feeder][der]['kW_BESS']} PF={DERs[feeder][der]['pf']}"

    # Solve the system
    Text.Command = "Solve"

    # Check convergence
    if Solution.Converged == False:
        print("Warning: Solution didn't converge!", flush=True)
    else:
        print(f"Solution converged at feeder {feeder}!", flush=True)

    return Circuit
