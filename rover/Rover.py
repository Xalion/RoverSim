from rover.RoverHelpers import compute_energy_drain


class Rover:
    """Contains the mechanism that controls the rover"""
    def __init__(self):
        self.default_battery_level = 100
        self.battery_level = self.default_battery_level
        self.location = [0.0, 0.0, 0.0]
        self.battery_base_movement = 10
        self.max_height_change = 100
        self.mass = 185

    def reset_battery(self):
        self.battery_level = self.default_battery_level

    def get_movement_direction(self):
        # Logic for movement goes here.  You are allowed to store whatever you want.  You are not allowed to change any
        # of the self variables.  They are here for your information only.  They will be adjusted by the simulation.

        # direction must be set to NORTH, SOUTH, EAST, or WEST
        direction = "NORTH"

        # This must be the last statement in this function.
        return direction

    def move_rover(self, new_location):
        battery_adjustment = compute_energy_drain(new_location, self.location, self)
        self.location = new_location
        self.battery_level = self.battery_level - battery_adjustment
