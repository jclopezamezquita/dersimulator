from dss import DSS
import numpy as np
import os.path
import json
import math
import sys


config = json.load(open("config.json"))
PATH = config["PATH"]


def run(feeder):
    # Start openDSS
    DSS.Start(0)

    # Get references to the main classes to make code shorter
    Text = DSS.Text
    Circuit = DSS.ActiveCircuit
    Solution = DSS.ActiveCircuit.Solution

    # Initilize matplot
    DSS.ClearAll()
    Text.Command = f"Redirect {PATH}/{feeder}_static/Master.dss"

    # Solve the system
    Text.Command = "Solve"

    # Check convergence
    if Solution.Converged == False:
        print("Warning: Solution didn't converge!", flush=True)
    else:
        print(f"Solution converged at feeder {feeder}!", flush=True)

    return Circuit
