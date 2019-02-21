import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt
# noinspection PyUnresolvedReferences
from mpl_toolkits.mplot3d import Axes3D  # This is used to import 3D projection


class GriddedTopographicalMap:
    """Defines a map that is divided into a regular grid and has topographic information"""
    def __init__(self, x_grid_div, y_grid_div, min_alt, max_alt, smoothing=2):
        self.x_grid_div = x_grid_div
        self.y_grid_div = y_grid_div
        self.min_alt = min_alt
        self.max_alt = max_alt

        unscaled = np.random.random((self.x_grid_div, self.y_grid_div))
        alt_scale = self.max_alt - self.min_alt
        unscaled = np.multiply(unscaled, alt_scale)
        self.height_map = np.add(unscaled, self.min_alt)

        self.height_map = ndimage.gaussian_filter(self.height_map, smoothing, mode='nearest')

    def plot(self):
        x, y = np.meshgrid(range(self.x_grid_div), range(self.y_grid_div))
        plot = plt.figure()
        fig = plot.add_subplot(111, projection='3d')
        fig.plot_surface(x, y, self.height_map)
        plot.show()

    def get_height(self, grid_location):
        return self.height_map[grid_location[0], grid_location[1]]

    def is_valid_location(self, grid_location):
        # implement
