# Container Terminal Simulation

This is a simulation of container terminal using SimPy. The goal of the simulation is to model the arrival and unloading of vessels at the terminal, as well as the use of cranes and trucks for handling containers.

## Installation

To run the simulation, you'll need to have Python 3.x and SimPy installed.

You can clone the repository and install the required libraries as follows:

1.  git clone https://github.com/chinmaya-ku-sahoo/Container-Terminal-Simulation.git
2.  cd Container-Terminal-Simulation
3.  pip install -r requirements.txt


## Running the Simulation

You can run the simulation by executing the `main.py` file:

```bash
python container_simulator.py
```

The simulation will run for a povided duration and will output logs of various events such as vessel arrivals, berthing, unloading, and truck assignments.

## Simulation Details

- Vessels arrive at the terminal following an exponential distribution with an average arrival interval of 5 hours.
- Each vessel carries 150 containers that need to be unloaded.
- There are 2 berth slots available at the terminal.
- There are 2 quay cranes available for unloading containers from vessels.
- There are 3 trucks available for transporting containers from cranes to the yard blocks.
- It takes a crane 3 minutes to move one container.
- It takes a truck 6 minutes to drop off a container at the yard block and return.

## Assumptions

- Each tick in the simulation represents 1 minute of time.
- Cranes and trucks are infinitely available and do not require maintenance or downtime.
- There is no variability in the time taken for berthing, unloading, or truck transportation.
