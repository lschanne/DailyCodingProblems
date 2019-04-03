'''
March 15, 2019

You are given an array of non-negative integers that represents a
two-dimensional elevation map where each element is unit-width wall and the
integer is the height. Suppose it will rain and all spots between two walls get
filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1)
space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the
middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2
in the second, and 3 in the fourth index (we cannot hold 5 since it would run
off to the left), so we can trap 8 units of water.
'''

def compute_trapped_water(elevation_map):
    units_of_water = 0
    biggest_wall = 0
    for wall in elevation_map:
        if wall > biggest_wall:
            biggest_wall = wall
        else:
            units_of_water += biggest_wall - wall

    return units_of_water

if __name__ == '__main__':
    import sys
    elevation_map = list(map(int, sys.argv[1:]))
    print('elevation map: {}'.format(elevation_map))
    print('trapped units of water: {}'.format(
        compute_trapped_water(elevation_map)
    ))
