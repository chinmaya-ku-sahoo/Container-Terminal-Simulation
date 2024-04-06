import simpy
import random

AVERAGE_ARRIVAL_INTERVAL = 300  # 5 hours
NUM_TRUCKS = 3

class Vessel:
    """Class representing a vessel in the container terminal simulation."""

    def __init__(self, env, name):
        """Initialize a vessel with the given name and environment."""
        self.env = env
        self.name = name
        self.containers = 150

    def berth_vessel(self, berth):
        """Process for berthing the vessel at a berth."""
        
        req = berth.request()
        yield req
        print(f"{self.env.now}: {self.name} berthed")
        yield self.env.timeout(0.1)
        berth.release(req)

    def unload_containers(self, crane, truck):
        """Process for unloading containers from the vessel."""
        
        print(f"{self.env.now}: Unloading started for {self.name}\n")
        while self.containers:
            req = crane.request()
            yield req
            yield self.env.timeout(3)
            self.containers -= 1
            print(f"{self.env.now}: {150-self.containers} container unloaded from {self.name}")
            crane.release(req)

            req = truck.request()
            yield req
            print(f"{self.env.now}: Container assigned to truck")
            yield self.env.timeout(6)
            print(f"{self.env.now}: Truck returned")
            truck.release(req)

def vessel_generator(env, berth, crane, trucks):
    """Generator function for creating vessels and assigning them to berths and cranes."""

    vessel_count = 0
    while True:

        vessel_count += 1
        vessel_name = f"Vessel-{vessel_count}"
        vessel = Vessel(env, vessel_name)

        env.process(vessel.berth_vessel(berth))
        env.process(vessel.unload_containers(crane, random.choice(trucks)))

        arrival_interval = random.expovariate(1/AVERAGE_ARRIVAL_INTERVAL)
        yield env.timeout(arrival_interval)


def main():
    SIMULATION_TIME = input("Provide the simulation time in minutes: ")
    if not SIMULATION_TIME.isdigit():
        print("The input could not be parsed. Please provide an integer value.")
    
    else:    
        env = simpy.Environment()
        berth = simpy.Resource(env, capacity=2)
        crane = simpy.Resource(env, capacity=2)
        trucks = [simpy.Resource(env, capacity=1) for _ in range(NUM_TRUCKS)]

        env.process(vessel_generator(env, berth, crane, trucks))
        env.run(until=SIMULATION_TIME)


if __name__ == "__main__":
    main()
