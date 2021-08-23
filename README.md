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


| key | key values | how to configure |
| ------ | ------ |------ | 
| cell | cell | cell |
| cell | cell | cell |

![alt-text](doc/Input.png)


## References


## Observations: 

<div>Icons made by <a href="https://www.flaticon.com/authors/wanicon" title="wanicon">wanicon</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>




## Running the simulations
