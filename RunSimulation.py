import map.GriddedTopographicalMap as GTM
import rover.Rover as Rover
import engine.Engine as Engine


def main():
    map_number = 15
    mp = GTM.GriddedTopographicalMap(10, 10, 0, 100, map_number)
    mp.plot()
    rover = Rover.Rover()
    engine = Engine.Engine(rover, mp)

    engine.run_sim()

    mp.plot_visited()
    print("Total Locations Visited", engine.visited_locations)


if __name__ == '__main__':
    main()
