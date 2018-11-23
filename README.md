# imt-capitrain

Research project around fog and edge computing. The aim of this project is to improve data movement in a fog architecture, with a central controller, that manages an index of cached dataset among distributed and distant servers, and help moving dataset considering network speeds and server load in terms of storage space.

## Installation

Before using this repositry, install [batsim](https://gitlab.inria.fr/batsim/batsim) using [nix](https://batsim.readthedocs.io/en/latest/installation.html#installation), as well as Python3.

Then clone the pybatsim temperature branch.

```bash
git clone --branch temperature https://gitlab.inria.fr/batsim/pybatsim.git
```

**Warning :** We developed our scheduler with pybatsim in on this [commit](https://gitlab.inria.fr/batsim/pybatsim/commit/cd41c625b444d04e99617d4238f92ca750bae80d). It seems new changes introduced regressions.

Then setup a virtual python environment and install this dependencies using pip3 :

```bash
pip3 install docopt zmq procset redis sortedcontainers matplotlib evalys
```

And finally, clone this repository:

```bash
git clone https://github.com/LouisAuneau/IMT-capitrain.git
```

## Launch simulation

To start our scheduler with pybatsim, first you have to start _batsim_ from our repository's folder:

```bash
batsim -p platform.xml -e visualization/out/imt --config_file batsim_config.txt --allow-time-sharing
```

Then start pybatsim from its directory :

```bash
python3 launcher.py {absolute_path_to_our_repo}/scheduler/StorageScheduler.py
```

## Visualize simulation results

To visualize data from the the simulation, go to the vizualisation directory and type:

```bash
python3 visualyze.py
```

The visualization is composed of 2 windows :

### Storage

It shows the load of each storage by time.

### Jobs

It shows 4 graphs :

- Resource utilisation by time
- Jobs queue size by time
- Jobs details
- A gantt chart of jobs execution

## Todos

- In the ON_SIMULATION_BEGINS callback, get the links between all entities to draw a network graph showing all throughputs.

- Write unit tests
