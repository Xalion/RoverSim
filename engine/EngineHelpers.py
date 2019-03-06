def resolve_direction(x):
    direction_dictionary =  {
        "NORTH": [1, 0],
        "SOUTH": [-1, 0],
        "EAST": [0, 1],
        "WEST": [0, -1]
    }

    return direction_dictionary.get(x)
