'''
May 27, 2019

Given a string and a set of characters, return the shortest substring
containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i},
you should return "aeci".

If there is no substring containing all the characters in the set, return null.
'''

def find_shortest_substring_with_chars(string, char_set):
    if not char_set:
        return ''

    for length in range(1, len(string) + 1):
        start_idx = 0
        end_idx = start_idx + length

        char_count = {c: 0 for c in char_set}
        for c in string[:length]:
            if c in char_count:
                char_count[c] += 1

        while True:
            if all(char_count.values()):
                return string[start_idx:end_idx]

            if end_idx < len(string):
                c = string[end_idx]
                if c in char_count:
                    char_count[c] += 1
                end_idx += 1
            else:
                break

            c = string[start_idx]
            if c in char_count:
                char_count[c] -= 1
            start_idx += 1

if __name__ == '__main__':
    test_cases = []

    # test 0
    test_cases.append({
        'string': 'figehaeci',
        'char_set': {'a', 'e', 'i'},
        'result': 'aeci',
    })

    # test 1
    test_cases.append({
        'string': '',
        'char_set': {},
        'result': '',
    })

    # test 2
    test_cases.append({
        'string': 'abc',
        'char_set': {'d'},
        'result': None,
    })

    # test 3
    test_cases.append({
        # Not that this use case is part of the design spec, but just to
        # demonstrate how it functions here
        'string': 'figehaeci',
        'char_set': 'aeiaeiaei',
        'result': 'aeci',
    })

    # test 4
    test_cases.append({
        'string': 'the quick brown fox jumps over the lazy brown dog',
        'char_set': 'abcdefghijklmnopqrstuvwxyz',
        'result': 'quick brown fox jumps over the lazy brown dog',
    })

    all_passed = True
    for idx, test_case in enumerate(test_cases):
        string = test_case['string']
        char_set = test_case['char_set']
        expected_result = test_case['result']
        try:
            result = find_shortest_substring_with_chars(string, char_set)
        except Exception:
            print('test #{} threw an exception!'.format(idx))
            all_passed = False
        else:
            if result != expected_result:
                print('test #{} failed!'.format(idx))
                all_passed = False

    if all_passed:
        print('All tests passed!')