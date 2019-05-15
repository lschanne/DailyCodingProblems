'''
May 11, 2019

A rule looks like this:
A NE B
This means this means point A is located northeast of point B.

A SW C
means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate.

For example:
A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.
'''

CARDINAL_DIRECTIONS = {'N', 'S', 'E', 'W'}
OPPOSITES = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E',
}

# Since this function will likely already be complex, we'll assume that the
# list of rules is properly formatted
def is_valid_cardinal_rules(rules):
    # create a map of the "world" created by the rules
    mapp = {}

    def _update_mapp(source, direction, dest):
        opposite = OPPOSITES[direction]
        if source not in mapp:
            mapp[source] = {d: set() for d in CARDINAL_DIRECTIONS}

        # the rule already exists
        elif dest in mapp[source][direction]:
            return True

        # the rule contradicts a previous rule
        elif dest in mapp[source][opposite]:
            return False

        # add the rule
        mapp[source][direction].add(dest)

        # apply rule to other locations that are in the opposite direction
        # from source
        for location in mapp[source][opposite]:
            if not _update_mapp(location, direction, dest):
                return False

        return True

    for rule in rules:
        source, directions, dest = rule.split()
        for direction in directions.upper():
            opposite = OPPOSITES[direction]
            # apply rule
            if not _update_mapp(source, direction, dest):
                return False

            # apply the congruency rule going the opposite direction
            if not _update_mapp(dest, opposite, source):
                return False

    return True

if __name__ == '__main__':
    test_objects = []

    # test 0
    rules = ['A NE B']
    is_valid = True
    test_objects.append((rules, is_valid))

    # test 1
    rules = ['A SW C']
    is_valid = True
    test_objects.append((rules, is_valid))

    # test 2
    rules = ['A NS B']
    is_valid = False
    test_objects.append((rules, is_valid))

    # test 3
    rules = [
        'A N B',
        'B NE C',
        'C N A',
    ]
    is_valid = False
    test_objects.append((rules, is_valid))

    # test 4
    rules = [
        'A NW B',
        'A N B',
    ]
    is_valid = True
    test_objects.append((rules, is_valid))

    all_passed = True
    for test_number, (rules, expected_result) in enumerate(test_objects):
        try:
            result = is_valid_cardinal_rules(rules)
        except Exception:
            print('test #{} threw an exception!'.format(test_number))
            all_passed = False
        else:
            if result != expected_result:
                print('test #{} failed!'.format(test_number))
                all_passed = False

    if all_passed:
        print('All tests passed!')
