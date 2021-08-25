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
| Loads file name | <p>string with the names of the json files that contain the circuit load data. For each feeder folder, you must have the same file name. "None" if there is no file</p> |
| PVs file name | <p>string with the names of the json files that contain the circuit generation data. For each feeder folder, you must have the same file name. "None" if there is no file</p>  |
| Load curves | <p>string containing the path to the json file with the demand multiplier curves for time-series analysis. The same file should be used for all loads of all feeders. "None" if there is no file. </p>|
| PV curves | <p>string containing the path to the json file with the generation multiplier curves for time-series analysis. The same file should be used for all loads of all feeders. "None" if there is no file. </p>|

**Table 2:** Configuration dictionary for the _Simulation_ key
| key | key values |
| ------ | ------ |
| Type | <p> Type of simulation (snapshot or time-series). Snapshot considers only a single simulation and time-series considers a time variation according to the load, generation and DERs operation curves. </p> |
| Output format | <p> Data output format (json or dataframe). The dataframe (csv) output format is only possible in snapshot simulations. </p> |
| Datetime | <p> Starting time of the simulation. Used to make simulations over time. </p> |
| Time step | <p> Simulation time step in minutes. </p> |
| Samples | <p> Total number of samples. </p> | 

**Table 3:** Configuration dictionary for the _DERs_ key

| key | key values |
| ------ | ------ |
| Scenario | <p>String containing the path to the json file with the data for all the DERs. "None" if there is no file.                                  </p> |
| Operation | <p>String containing the path to the json file with the DER operation. "None" if there is no file.                                  </p> |

**Table 4:** Configuration dictionary for the _Results_ key

| key | key values |
| ------ | ------ |
| Scenario | <p>String with the path to the json file containing the nodes and elements that should appear in the output file. Enter "All" to display all. Note: Although they are separate, the json file must be the same for the nodes and elements.</p>|
| Operation | <p>String with the path to the json file containing the elements and elements that should appear in the output file. Enter "All" to display all. Note: Although they are separate, the json file must be the same for the nodes and elements.</p>|

### Input Files

![alt-text](doc/Input.png)

**Figure 2:** Suggested folders and files organization for simulation


## Examples

The examples are downloaded with the repository. Details are at the following links:

[Example 1](https://gitlab.com/smart-grids-tools/dersimulator/-/tree/main/examples/ex1): Snapshot simulation of the IEEE 4-bar network;

[Example 2](https://gitlab.com/smart-grids-tools/dersimulator/-/tree/main/examples/ex2): 96-sample time-series simulation of IEEE 4-bar network;

[Example 3](https://gitlab.com/smart-grids-tools/dersimulator/-/tree/main/examples/ex3): 96-sample time-series simulation of the 4-bar IEEE grid with photovoltaic generation;

[Example 4](https://gitlab.com/smart-grids-tools/dersimulator/-/tree/main/examples/ex4): 96-sample time-series simulation of the IEEE 4-bar network with charging station;


## References

[1] dss-python. Available at https://pypi.org/project/dss-python 

[2] IEEE test cases. Available at https://github.com/tshort/OpenDSS/tree/master/Distrib/IEEETestCases 

## Observations: 

<div>Icons made by <a href="https://www.flaticon.com/authors/wanicon" title="wanicon">wanicon</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>




## Running the simulations
