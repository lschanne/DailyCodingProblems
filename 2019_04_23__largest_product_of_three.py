'''
April 23, 2019

Given a list of integers, return the largest product that can be made by
multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since
that's -10 * -10 * 5.
'''

# Well the function is a bit verbose, but given the explicity of the problem
# statement, I think it is appropriate. Adding in flexibility for how many
# integers you want to be able to multiply is unneeded complication
def get_largest_product_of_three(input_list):
    if len(input_list) < 3:
        return None

    largest_negative = 0
    second_largest_negative = 0
    largest_positive = 0
    second_largest_positive = 0
    third_largest_positive = 0

    for x in input_list:
        if x < largest_negative:
            second_largest_negative = largest_negative
            largest_negative = x
        elif x < second_largest_negative:
            second_largest_negative = x
        elif x > largest_positive:
            third_largest_positive = second_largest_positive
            second_largest_positive = largest_positive
            largest_positive = x
        elif x > second_largest_positive:
            third_largest_positive = second_largest_positive
            second_largest_positive = x
        elif x > third_largest_positive:
            third_largest_positive = x

    negative_product = largest_negative * second_largest_negative
    positive_product = second_largest_positive * third_largest_positive
    if negative_product > positive_product:
        positive_product = negative_product

    positive_product *= largest_positive
    return positive_product

if __name__ == '__main__':
    import sys
    input_list = [int(x) for x in sys.argv[1:]]
    print('input list: {}'.format(input_list))
    print('result: {}'.format(get_largest_product_of_three(input_list)))
