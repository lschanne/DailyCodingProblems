'''
March 6, 2019

Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

# Seems like there's probably a better way...
def get_min_rooms(schedule):
    # O(n) for this part
    schedule_dict = {}
    for start, end in schedule:
        schedule_dict[start] = schedule_dict.get(start, 0) + 1
        schedule_dict[end] = schedule_dict.get(end, 0) - 1

    # I believe sorting is O(n*log_n)
    # So this part is O(n*log_n + n) = O(n*log_n)
    result = 0
    concurrent_classes = 0
    for key in sorted(schedule_dict.keys()):
        concurrent_classes += schedule_dict[key]
        if concurrent_classes > result:
            result = concurrent_classes

    # I gotta tell you though, just calling this O(n*log_n) is misleading in
    # my mind. It is O(n*log_n + 2*n). It would take quite a large n for
    # 2*n to be eclipsed by n*log_n
    # Even at n=1000000, the difference is ~14.5%
    # Just trying to compute how large `n` has to be to get <1% difference
    # overflows the Python int
    # At n=1000000000000000000, the difference is ~4.8% (still not nothing!)
    return result

if __name__ == '__main__':
    import sys
    schedule = [list(map(int, x.split(','))) for x in sys.argv[1:]]
    print('schedule: {}'.format(schedule))
    result = get_min_rooms(schedule)
    print('minimum rooms required: {:.0f}'.format(result))
