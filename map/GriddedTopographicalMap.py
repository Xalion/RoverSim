import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt
# noinspection PyUnresolvedReferences
from mpl_toolkits.mplot3d import Axes3D  # This is used to import 3D projection


class GriddedTopographicalMap:
    """Defines a map that is divided into a regular grid and has topographic information"""
    def __init__(self, x_grid_div, y_grid_div, min_alt, max_alt, seed, smoothing=2):
        self.x_grid_div = x_grid_div
        self.y_grid_div = y_grid_div
        self.min_alt = min_alt
        self.max_alt = max_alt

        np.random.seed(seed)

        unscaled = np.random.random((self.x_grid_div, self.y_grid_div))
        alt_scale = self.max_alt - self.min_alt
        unscaled = np.multiply(unscaled, alt_scale)
        self.height_map = np.add(unscaled, self.min_alt)

        self.height_map = ndimage.gaussian_filter(self.height_map, smoothing, mode='nearest')
        self.visited_map = [[0 for i in range(self.x_grid_div)] for j in range(self.y_grid_div)]
        self.reset_visited()

    def get_map_coords(self, grid_loc):
        return [grid_loc[0], grid_loc[1], self.height_map[grid_loc[0], grid_loc[1]]]

    def get_grid_location(self, map_loc):
        return [map_loc[0], map_loc[1]]

    def plot(self):
        x, y = np.meshgrid(range(self.x_grid_div), range(self.y_grid_div))
        plot = plt.figure()
        fig = plot.add_subplot(111, projection='3d')
        fig.plot_surface(x, y, self.height_map)
        plot.show()

    def get_height(self, grid_location):
        return self.height_map[grid_location[0], grid_location[1]]

    def is_valid_location(self, grid_location, rover):
        if grid_location[0] < 0 or grid_location[0] >= self.x_grid_div:
            return False
        if grid_location[1] < 0 or grid_location[1] >= self.y_grid_div:
            return False
        new_z = self.height_map[grid_location[0], grid_location[1]]
        height_change = new_z - rover.location[2]
        if height_change > rover.max_height_change:
            return False

        return True

    def reset_visited(self):
        self.visited_map = [[0 for i in range(self.x_grid_div)] for j in range(self.y_grid_div)]

    def visit(self, location):
        self.visited_map[location[0]][location[1]] += 1

    def has_visited_grid_location(self, grid_location):
        return (False, True)[self.visited_map[grid_location[0]][grid_location[1]] > 0]

    def has_visisted_map_location(self, map_location):
        return self.has_visited_grid_location(self.get_grid_location(map_location))

    def plot_visited(self):
        color_map = np.array(self.visited_map)
        plt.imshow(color_map)
        plt.show()
