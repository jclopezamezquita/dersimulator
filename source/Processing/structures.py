from dss import DSS
import pandas as pd


def json_bus(Circuit, buslist):
    data = dict()
    for bar in buslist:
        Circuit.ActiveBus(bar)
        data.update(
            {
                bar: {
                    "VA": [],
                    "VB": [],
                    "VC": [],
                    "PA": [],
                    "PB": [],
                    "PC": [],
                    "QA": [],
                    "QB": [],
                    "QC": [],
                }
            }
        )
    return data


def json_elements(Circuit, elementslist):
    data = dict()
    for element in elementslist:
        Circuit.SetActiveElement(element)
        data.update(
            {
                element: {
                    "IA": [],
                    "IB": [],
                    "IC": [],
                    "PA": [],
                    "PB": [],
                    "PC": [],
                    "QA": [],
                    "QB": [],
                    "QC": [],
                    "kWLosses": [],
                    "kVArLosses": [],
                }
            }
        )
    return data
