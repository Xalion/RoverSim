

def compute_potential_drain(height_change, rover):
    mars_grav_constant = 3.177
    potential_change = height_change * rover.mass * mars_grav_constant / 10
    return (0, potential_change)[potential_change > 0]


def compute_energy_drain(old_loc, new_loc, rover):
    min_adjust = rover.battery_base_movement
    min_adjust += compute_potential_drain(new_loc[2] - old_loc[2], rover)
    return min_adjust
