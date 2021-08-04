from math import sqrt
from dss import DSS
import numpy as np
import math
import os


def get_power(Circuit, bar):
            #PA, QA, PB, QB, PC, QC
    
    Powers = [0, 0, 0, 0, 0, 0]
    if Circuit.ActiveBus.LoadList[0]:
        for load in Circuit.ActiveBus.LoadList:
            Circuit.SetActiveElement(load)
            CurrentPowers = Circuit.ActiveElement.Powers
            Powers = np.add(Powers, CurrentPowers[0:6])
            
    return Powers

def busdata(Circuit, bus, buslist):
    for bar in buslist:
        Circuit.SetActiveBus(bar)
        Voltages = Circuit.ActiveBus.puVoltages
        bus[bar]['VA'].append(sqrt(Voltages[0]**2+Voltages[1]**2))
        bus[bar]['VB'].append(sqrt(Voltages[2]**2+Voltages[3]**2))
        bus[bar]['VC'].append(sqrt(Voltages[4]**2+Voltages[5]**2))
        
        Powers = get_power(Circuit, bar)
        bus[bar]['PA'].append(Powers[0])
        bus[bar]['PB'].append(Powers[2])
        bus[bar]['PC'].append(Powers[4])
        bus[bar]['QA'].append(Powers[1])
        bus[bar]['QB'].append(Powers[3])
        bus[bar]['QC'].append(Powers[5])
    return bus

def elementsdata(Circuit, elements, elementslist):
    for element in elementslist:
        Circuit.SetActiveElement(element)
        Currents = Circuit.ActiveElement.Currents
        elements[element]['IA'].append(sqrt(Currents[0]**2 + Currents[1]**2))
        elements[element]['IB'].append(sqrt(Currents[2]**2 + Currents[3]**2))
        elements[element]['IC'].append(sqrt(Currents[4]**2 + Currents[5]**2))
        Powers = Circuit.ActiveElement.Powers
        elements[element]['PA'].append(Powers[0])
        elements[element]['PB'].append(Powers[2])
        elements[element]['PC'].append(Powers[4])
        elements[element]['QA'].append(Powers[1])
        elements[element]['QB'].append(Powers[3])
        elements[element]['QC'].append(Powers[5])
    return elements