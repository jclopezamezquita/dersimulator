from dss import DSS
import pandas as pd


def json_bus(Circuit):
    data = dict()
    for bar in Circuit.AllBusNames:
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


def json_elements(Circuit):
    data = dict()
    for element in Circuit.AllElementNames:
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
