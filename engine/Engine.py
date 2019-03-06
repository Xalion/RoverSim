import random
from engine.EngineHelpers import resolve_direction


class Engine:
    """Contains the time loop that drives the simulation"""
    def __init__(self, rover, topo_map):
        self.visited_locations = 0
        self.rover = rover
        self.map = topo_map
        self.starting_loc = [random.randint(0, topo_map.x_grid_div-1), random.randint(0, topo_map.y_grid_div-1)]
        self.current_loc = self.starting_loc

    def reset_rover(self):
        self.rover.location = [self.starting_loc[0], self.starting_loc[1], self.map.get_height(self.starting_loc)]
        self.current_loc = self.starting_loc.copy()
        self.rover.battery_level = self.rover.default_battery_level
        self.visited_locations = 0
        self.map.reset_visited()

    def step(self):
        if self.rover.battery_level <= 0.0:
            return False

        direction = self.rover.get_movement_direction()

        possible_grid_loc = self.current_loc

        grid_step = resolve_direction(direction)
        possible_grid_loc[0] += grid_step[0]
        possible_grid_loc[1] += grid_step[1]

        if self.map.is_valid_location(possible_grid_loc, self.rover):
            map_loc = self.map.get_map_coords(possible_grid_loc)
            self.rover.move_rover(map_loc)
            self.current_loc = possible_grid_loc

            if not self.map.has_visited_grid_location(possible_grid_loc):
                self.visited_locations += 1
                self.map.visit(possible_grid_loc)

            return True

        return False

    def run_sim(self):
        self.reset_rover()
        running = True
        while running:
            running = self.step()
            if self.current_loc == self.starting_loc:
                self.rover.reset_battery()







