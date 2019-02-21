from enum import Enum


class Rover:
    """Contains the mechanism that controls the rover"""
    def __init__(self):
        self.battery_level = 100
        self.location = [0.0, 0.0, 0.0]

    def get_movement_direction(self):

        # Logic for movement goes here.  You are allowed to store whatever you want.  You are not allowed to access
        # self.location or self.battery_level.  They are here for your convenience only.

        # direction must be set to NORTH, SOUTH, EAST, or WEST
        direction = "NORTH"

        # This must be the last statement in this function.
        return direction

    def move_rover(self, new_location):
        # TODO here