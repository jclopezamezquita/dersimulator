from dss import DSS
import pandas as pd


def json_bus(buslist):
    data = {"time-step": []}
    for bar in buslist:
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


def json_elements(elementslist):
    data = {"time-step": []}
    for element in elementslist:
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
