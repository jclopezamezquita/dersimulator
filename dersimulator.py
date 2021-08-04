from source.Processing import measurements
from source.Processing import structures
from source.LoadFlow import powerflow
import json
import os



config = json.load(open("config.json"))
feeder = config['DSS']["feeders"][0]

Circuit = powerflow.run(feeder)

# Define structures
bus = structures.bus(Circuit)
elements = structures.elements(Circuit)

# Get measures
bus = measurements.busdata(Circuit, bus, Circuit.AllBusNames)
elements = measurements.elementsdata(Circuit, elements, Circuit.AllElementNames)

if not os.path.exists('Estudos/'):
    os.makedirs('Estudos/')

# Save files
with open('Estudos/bus.json', 'w') as f:
    json.dump(bus,f, indent=2)

with open('Estudos/elements.json', 'w') as f:
    json.dump(elements, f, indent=2)

a = 1

