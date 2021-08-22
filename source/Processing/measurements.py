from math import sqrt
from dss import DSS
import pandas as pd
import numpy as np
import math
import os


def get_power(Circuit, bar):
    # PA, QA, PB, QB, PC, QC

    Powers = [0, 0, 0, 0, 0, 0]
    if Circuit.ActiveBus.LoadList[0]:
        for load in Circuit.ActiveBus.LoadList:
            Circuit.SetActiveElement(load)
            CurrentPowers = Circuit.ActiveElement.Powers
            Powers = np.add(Powers, CurrentPowers[0:6])

    return Powers


def json_busdata(Circuit, bus, buslist):
    for bar in buslist:
        Circuit.SetActiveBus(bar)
        Voltages = Circuit.ActiveBus.puVoltages
        bus[bar]["VA"].append(sqrt(Voltages[0] ** 2 + Voltages[1] ** 2))
        bus[bar]["VB"].append(sqrt(Voltages[2] ** 2 + Voltages[3] ** 2))
        bus[bar]["VC"].append(sqrt(Voltages[4] ** 2 + Voltages[5] ** 2))

        Powers = get_power(Circuit, bar)
        bus[bar]["PA"].append(Powers[0])
        bus[bar]["PB"].append(Powers[2])
        bus[bar]["PC"].append(Powers[4])
        bus[bar]["QA"].append(Powers[1])
        bus[bar]["QB"].append(Powers[3])
        bus[bar]["QC"].append(Powers[5])
    return bus


def json_elementsdata(Circuit, elements, elementslist):
    for element in elementslist:
        Circuit.SetActiveElement(element)
        Currents = Circuit.ActiveElement.Currents
        elements[element]["IA"].append(sqrt(Currents[0] ** 2 + Currents[1] ** 2))
        elements[element]["IB"].append(sqrt(Currents[2] ** 2 + Currents[3] ** 2))
        elements[element]["IC"].append(sqrt(Currents[4] ** 2 + Currents[5] ** 2))
        Powers = Circuit.ActiveElement.Powers
        elements[element]["PA"].append(Powers[0])
        elements[element]["PB"].append(Powers[2])
        elements[element]["PC"].append(Powers[4])
        elements[element]["QA"].append(Powers[1])
        elements[element]["QB"].append(Powers[3])
        elements[element]["QC"].append(Powers[5])
        Losses = Circuit.ActiveCktElement.Losses
        elements[element]["kWLosses"].append(Losses[0] / 1000)
        elements[element]["kVArLosses"].append(Losses[1] / 1000)

    return elements


def dataframe_busdata(Circuit, buslist):
    columns = ["node", "VA", "VB", "VC", "PA", "PB", "PC", "QA", "QB", "QC"]
    df = pd.DataFrame(columns=columns)
    for bar in buslist:
        Circuit.SetActiveBus(bar)
        Voltages = Circuit.ActiveBus.puVoltages
        Powers = get_power(Circuit, bar)
        data = {
            "node": bar,
            "VA": sqrt(Voltages[0] ** 2 + Voltages[1] ** 2),
            "VB": sqrt(Voltages[2] ** 2 + Voltages[3] ** 2),
            "VC": sqrt(Voltages[4] ** 2 + Voltages[5] ** 2),
            "PA": Powers[0],
            "PB": Powers[2],
            "PC": Powers[4],
            "QA": Powers[1],
            "QB": Powers[3],
            "QC": Powers[5],
        }
        df = df.append(data, ignore_index=True)
    return df


def dataframe_elementsdata(Circuit, elementslist):
    columns = [
        "element",
        "IA",
        "IB",
        "IC",
        "PA",
        "PB",
        "PC",
        "QA",
        "QB",
        "QC",
        "kWLosses",
        "kVArLosses",
    ]
    df = pd.DataFrame(columns=columns)
    for element in elementslist:
        Circuit.SetActiveElement(element)
        Currents = Circuit.ActiveElement.Currents
        Powers = Circuit.ActiveElement.Powers
        Losses = Circuit.ActiveCktElement.Losses
        data = {
            "element": element,
            "IA": sqrt(Currents[0] ** 2 + Currents[1] ** 2),
            "IB": sqrt(Currents[2] ** 2 + Currents[3] ** 2),
            "IC": sqrt(Currents[4] ** 2 + Currents[5] ** 2),
            "PA": Powers[0],
            "PB": Powers[2],
            "PC": Powers[4],
            "QA": Powers[1],
            "QB": Powers[3],
            "QC": Powers[5],
            "kWLosses": Losses[0] / 1000,
            "kVArLosses": Losses[1] / 1000,
        }
        df = df.append(data, ignore_index=True)
    return df
