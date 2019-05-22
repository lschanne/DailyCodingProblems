'''
May 16, 2019

We're given a hashmap associating each courseId key with a list of courseIds
values, which represents that the prerequisites of courseId are courseIds.
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given
{'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
should return ['CSC100', 'CSC200', 'CSCS300'].
'''

def courses_in_order(course_hashmap):
    ordered_courses = []

    return ordered_courses

if __name__ == '__main__':
    test_cases = []

    # test 0
    course_hashmap = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': [],
    }
    expected_result = ['CSC100', 'CSC200', 'CSC300']
    test_cases.append((course_hashmap, expected_result))

    # test 1
    course_hashmap = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': ['CSC300'],
    }
    expected_result = None
    test_cases.append((course_hashmap, expected_result))

    all_passed = True
    for idx, (course_hashmap, expected_result) in enumerate(test_cases):
        try:
            result = courses_in_order(course_hashmap)
        except Exception:
            print('test #{} threw an exception!'.format(idx))
            all_passed = False
        else:
            if result != expected_result:
                print('test #{} failed!'.format(idx))
                all_passed = False

    if all_passed:
        print('All {} tests passed!'.format(len(test_cases)))