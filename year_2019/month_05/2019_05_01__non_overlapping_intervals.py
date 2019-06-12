'''
May 1, 2019

Given a list of possibly overlapping intervals, return a new list of intervals
where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return
[(1, 3), (4, 10), (20, 25)].
'''

# So it's not super performant, and there probably is a better way to do this,
# but the spec doesn't say anything specific about performance, so I guess I
# will leave this as is
def merge_overlapping_intervals(input_list):
    output_list = []

    for start, end in input_list:
        pop_list = []
        for idx, (start2, end2) in enumerate(output_list):
            if start2 >= start and end2 <= end:
                pop_list.append(idx)
            elif start >= start2 and end <= end2:
                break
        else:
            for idx in reversed(pop_list):
                output_list.pop(idx)
            output_list.append((start, end))

    return output_list

if __name__ == '__main__':
    import sys
    input_list = []
    for idx in range(1, len(sys.argv), 2):
        input_list.append(tuple(map(int, sys.argv[idx:idx + 2])))

    print('input list: {}'.format(input_list))
    print('output list: {}'.format(merge_overlapping_intervals(input_list)))
