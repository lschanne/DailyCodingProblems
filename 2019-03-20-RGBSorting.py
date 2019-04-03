'''
March 20, 2019

Given an array of strictly the characters 'R', 'G', and 'B', segregate the
values of the array so that all the Rs come first, the Gs come second, and the
Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

def rgb_sort(rgb_list):
    idx = 0
    R_idx = 0
    B_idx = len(rgb_list) - 1
    while idx <= B_idx:
        while rgb_list[idx] in 'RB':
            if rgb_list[idx] == 'R':
                if R_idx == idx:
                    R_idx += 1
                    break
                rgb_list[idx], rgb_list[R_idx] = rgb_list[R_idx], rgb_list[idx]
                R_idx += 1

            elif rgb_list[idx] == 'B':
                if idx == B_idx:
                    break
                rgb_list[idx], rgb_list[B_idx] = rgb_list[B_idx], rgb_list[idx]
                B_idx -= 1

        idx += 1

    return rgb_list




if __name__ == '__main__':
    import sys
    rgb_list = sys.argv[1:]
    print('initial list: {}'.format(rgb_list))
    print('sorted list: {}'.format(rgb_sort(rgb_list)))
