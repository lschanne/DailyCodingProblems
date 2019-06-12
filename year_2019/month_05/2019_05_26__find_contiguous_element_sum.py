'''
May 26, 2019

Given a list of integers and a number K, return which contiguous elements of
the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should
return [2, 3, 4], since 2 + 3 + 4 = 9.
'''

def find_contiguous_element_sum(input_list, K):
    if not K:
        return []

    for num_elements in range(1, len(input_list) + 1):
        start_idx = 0
        end_idx = start_idx + num_elements
        this_sum = sum(input_list[start_idx:end_idx])
        while True:
            if this_sum == K:
                return input_list[start_idx:end_idx]

            this_sum -= input_list[start_idx]
            start_idx += 1
            if end_idx < len(input_list):
                this_sum += input_list[end_idx]
                end_idx += 1
            else:
                break

    return None

if __name__ == '__main__':
    test_cases = []

    # test 0
    # So you can see by this test that my function is a bit different from the
    # expected function. Mine prioritizes smaller subsets, whereas the expected
    # function prioritizes (seemingly) the first such subarray. This difference
    # makes me wonder if there is a much better way to do this. Of course their
    # result would be obtained through a simple recursion, but I think that
    # would be less efficient
    test_cases.append({
        'input_list': [1, 2, 3, 4, 5],
        'K': 9,
        'expected_result': [4, 5]
    })

    # test 1
    test_cases.append({
        'input_list': [],
        'K': 0,
        'expected_result': []
    })

    # test 2
    test_cases.append({
        'input_list': [1, 2],
        'K': 4,
        'expected_result': None
    })

    # test 3
    test_cases.append({
        'input_list': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'K': 34,
        'expected_result': [7, 8, 9, 10]
    })

    # test 4
    test_cases.append({
        'input_list': [1, 1, 1, 1, 1, 1],
        'K': 3,
        'expected_result': [1, 1, 1]
    })

    all_passed = True
    for idx, test_case in enumerate(test_cases):
        input_list = test_case['input_list']
        K = test_case['K']
        expected_result = test_case['expected_result']
        result = find_contiguous_element_sum(input_list, K)
        try:
            result = find_contiguous_element_sum(input_list, K)
        except Exception:
            print('test #{} raised an exception!'.format(idx))
            all_passed = False
        else:
            if expected_result != result:
                print('test #{} failed!'.format(idx))
                all_passed = False
                print(result)

    if all_passed:
        print('All tests passed!')