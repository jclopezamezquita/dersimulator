# Distributed Energy Resources (DERs) Simulator and measurements

## Introduction

A program in Python that determines the state of grid operation with distributed Energy Resources (DERs).

The DERs that can be simulated in the program are:

- Charging Stations (CS);
- Photovoltaic Systems (PS);
- Battery Energy Store System (BESS);

The load flow is run through the [dss-python](https://pypi.org/project/dss-python/) library .

## Architecture

![alt-text](doc/Architecture.png)

**Figure 1:** DERSimulator Architecture


## Installation

_In Construction_

## Simulation Guide

<p>To perform the simulations you need to edit the json file `config.json` and the folder with the distribution network data and the existing DERs.</p>

<p>The configuration file is in json format and has the following main keys: _DSS_, _Simulation_, _DERs_ and _Results_. For each of these keys there is a dictionary with the parameters needed to perform different simulations.</p>

### Contents of the file config.json

**Table 1:** Configuration dictionary for the _DSS_ key
| key | key values |
| ------ | ------ |
| PATH | string with the path to the folder containing the feeders. |
| feeders | a list with the names of the folders containing the feeders' data. |
| Loads file name | <p>string with the names of the json files that contain the circuit load data. For each feeder folder, you must have the same file name.</p> |
| PVs file name | <p>string with the names of the json files that contain the circuit generation data. For each feeder folder, you must have the same file name.</p>  |
| Load curves | string containing the path to the json file with the demand multiplier curves for time-series analysis. The same file should be used for all loads of all feeders. |
| PV curves | string containing the path to the json file with the generation multiplier curves for time-series analysis. The same file should be used for all loads of all feeders. |

**Table 2:** Configuration dictionary for the _Simulation_ key
| key | key values |
| ------ | ------ |
| Type | <p> Type of simulation (snapshot or time-series). Snapshot considers only a single simulation and time-series considers a time variation according to the load, generation and DERs operation curves. </p> |
| Output format | <p> Data output format (json or dataframe). The dataframe (csv) output format is only possible in snapshot simulations. </p> |
| Datetime | <p> Starting time of the simulation. Used to make simulations over time. </p> |
| Time step | <p> Simulation time step in minutes. </p> |
| Samples | <p> Total number of samples. </p> | 

**Table 3:** Configuration

**Table 4:**


![alt-text](doc/Input.png)


## References


## Observations: 

<div>Icons made by <a href="https://www.flaticon.com/authors/wanicon" title="wanicon">wanicon</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>




## Running the simulations
