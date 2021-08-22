from source.Processing import dictionaries
################################################################################
from source import simulation
from datetime import datetime
from dateutil import parser
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
config = json.load(open('config.json'))

############################## Snapshott powerflow #############################
if config['Simulation']['Type'] == 'snapshot':
    print('Snapshot simulation')
    ########################## run snapshot powerflow ##########################
    for feeder in FEEDERs:
        simulation.snapshot(config, feeder, LOADs, PVs, DERs)


############################## Time-series powerflow ###########################
elif config['Simulation']['Type'] == 'time-series':
    if config['Simulation']['Output format'] != 'json':
        print(f'Only json format is supported for time-series simulation')
        sys.exit(0)
    if config['Simulation']['Datetime'] == 'Now':
        date = datetime.now()
    try:
        date = parser.parse(config['Simulation']['Datetime'])
    except:
        print('Date out of iso format')
        sys.exit(0)
    

print('End of simulation')
sys.exit(0)








    
