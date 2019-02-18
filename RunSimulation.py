import map.GriddedTopographicalMap as gtm
import matplotlib.pyplot as plt


def main():
    mp = gtm.GriddedTopographicalMap(10, 10, 0, 100)
    mp.plot()

if __name__ == '__main__':
    main()
