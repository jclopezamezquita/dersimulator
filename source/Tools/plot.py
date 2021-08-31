import matplotlib.pyplot as plt
from datetime import timedelta
from datetime import datetime
from dateutil import parser
import json
import os

def result_bus(config, date, feeder):
    if not os.path.exists(f"Results/{feeder}"):
        os.makedirs(f"Results/{feeder}")
    bus = json.load(open(f'Results/{feeder}_bus.json'))
    time_step = config['Simulation']['Time step']
    samples = config['Simulation']['Samples']
    x = [date + timedelta(minutes=time_step*i) for i in range(0, samples)]
    for bar in bus:
        if bar != 'time-step':
            ################## Plot voltages ###################################
            plt.plot(x, bus[bar]['VA'])
            plt.plot(x, bus[bar]['VB'])
            plt.plot(x, bus[bar]['VC'])
            plt.ylabel('Voltage [p.u]')
            plt.legend(['VA', 'VB', 'VC'])
            plt.gcf().autofmt_xdate()
            plt.savefig(f'Results/{feeder}/{bar}_voltages.png')
            plt.close('all')
            ################## Plot active power ###############################
            plt.plot(x, bus[bar]['PA'])
            plt.plot(x, bus[bar]['PB'])
            plt.plot(x, bus[bar]['PC'])
            plt.ylabel('Nodal Active Power [kW]')
            plt.legend(['PA', 'PB', 'PC'])
            plt.gcf().autofmt_xdate()
            plt.savefig(f'Results/{feeder}/{bar}_active_powers.png')
            plt.close('all')
            ################## Plot active power ###############################
            plt.plot(x, bus[bar]['QA'])
            plt.plot(x, bus[bar]['QB'])
            plt.plot(x, bus[bar]['QC'])
            plt.ylabel('Nodal Reactive Power [kVAr]')
            plt.legend(['QA', 'QB', 'QC'])
            plt.gcf().autofmt_xdate()
            plt.savefig(f'Results/{feeder}/{bar}_reactive_powers.png')
            plt.close('all')
    return

def result_elements(config, date, feeder):
    if not os.path.exists(f"Results/{feeder}"):
        os.makedirs(f"Results/{feeder}")
    elements = json.load(open(f'Results/{feeder}_elements.json'))
    time_step = config['Simulation']['Time step']
    samples = config['Simulation']['Samples']
    x = [date + timedelta(minutes=time_step*i) for i in range(0, samples)]
    for element in elements:
        if element != 'time-step':
            ################## Plot voltages ###################################
            plt.plot(x, elements[element]['IA'])
            plt.plot(x, elements[element]['IB'])
            plt.plot(x, elements[element]['IC'])
            plt.ylabel('Currents [A]')
            plt.legend(['IA', 'IB', 'IC'])
            plt.gcf().autofmt_xdate()
            plt.savefig(f'Results/{feeder}/{element}_currents.png')
            plt.close('all')
            ################## Plot active power ###############################
            plt.plot(x, elements[element]['PA'])
            plt.plot(x, elements[element]['PB'])
            plt.plot(x, elements[element]['PC'])
            plt.ylabel('Active Power [kW]')
            plt.legend(['PA', 'PB', 'PC'])
            plt.gcf().autofmt_xdate()
            plt.savefig(f'Results/{feeder}/{element}_active_powers.png')
            plt.close('all')
            ################## Plot active power ###############################
            plt.plot(x, elements[element]['QA'])
            plt.plot(x, elements[element]['QB'])
            plt.plot(x, elements[element]['QC'])
            plt.ylabel('Reactive Power [kVAr]')
            plt.legend(['QA', 'QB', 'QC'])
            plt.gcf().autofmt_xdate()
            plt.savefig(f'Results/{feeder}/{element}_reactive_powers.png')
            plt.close('all')
            ################## Plot Losses #####################################
            plt.plot(x, elements[element]['kWLosses'])
            plt.plot(x, elements[element]['kVArLosses'])
            plt.ylabel('Total Losses [kW/kVAr]')
            plt.legend(['kW', 'kVAr'])
            plt.gcf().autofmt_xdate()
            plt.savefig(f'Results/{feeder}/{element}_losses.png')
            plt.close('all')
    return