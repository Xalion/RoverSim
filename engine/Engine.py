import random


class Engine:
    """Contains the time loop that drives the simulation"""
    def __init__(self, rover, topo_map):
        self.rover = rover
        self.map = topo_map
        self.starting_loc = [random.randint(0, topo_map.x_grid_div), random.randint(0, topo_map.y_grid_div)]
        self.current_loc = self.starting_loc

    def reset_rover(self):
        self.rover.location = [self.starting_loc[0], self.starting_loc[1], self.map.get_height(self.starting_loc)]
        self.current_loc = self.starting_loc
        self.rover.battery_level = 100.0

    def step(self):
        # TODO here