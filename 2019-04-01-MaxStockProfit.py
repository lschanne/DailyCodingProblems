'''
April 1, 2019

Given a array of numbers representing the stock prices of a company in
chronological order, write a function that calculates the maximum profit you
could have made from buying and selling that stock once. You must buy before
you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could
buy the stock at 5 dollars and sell it at 10 dollars.
'''

import sys

def find_max_profit(prices):
    min_price = sys.maxint
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit

if __name__ == '__main__':
    prices = list(map(int, sys.argv[1:]))
    print('stock prices: {}'.format(prices))
    print('max profit: {}'.format(find_max_profit(prices)))
