from source import powerflow
import os, sys
import json


config = json.load(open("config.json"))
feeder = config["feeders"][0]

Circuit = powerflow.run(feeder)
a = 1
