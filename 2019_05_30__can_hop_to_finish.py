'''
May 30, 2019

Given an integer list where each number represents the number of hops you can
make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
'''

# wow this is underdefined.
# If I hop to a 2, can I choose to hop either 1 or 2 spaces?
# If I do only hop once, do I still have that residual hop from the 2?
# I will say Yes and No, respectively, since that seemingly yields the most
# technically challenging situtation

def can_hop_to_finish(hop_list):
    def _recurse(current_idx):
        if current_idx >= len(hop_list) - 1:
            return True

        for num_hops in range(1, hop_list[current_idx] + 1):
            if _recurse(current_idx + num_hops):
                return True

        return False

    return _recurse(0)

if __name__ == '__main__':
    import sys
    hop_list = [int(x) for x in sys.argv[1:]]
    print('hops: {}'.format(hop_list))
    print('can hop to finish: {}'.format(can_hop_to_finish(hop_list)))
