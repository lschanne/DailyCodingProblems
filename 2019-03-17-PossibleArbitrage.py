'''
March 17, 2019

Suppose you are given a table of currency exchange rates, represented as a 2D
array. Determine whether there is a possible arbitrage: that is, whether there
is some sequence of trades you can make, starting with some amount A of any
currency, so that you can end up with some amount greater than A of that
currency.

There are no transaction costs and you can trade fractional quantities.
'''

'''
So first I have to define what the exchange rates look like since the problem
statement doesn't do so explicitly. I think that a list of 3-item tuples
makes the most sense.
(starting_currency, ending_currency, multiplier)

So if you have X of currency A and wish to exchange to currency B, then you
find the (A, B, M) tuple in the exchange rates. Then you figure out that
you will have X * M of currency B.

Let's say that there is guaranteed to be no duplicate entries for A, B.
For example if there is an (A, B, M0) entry, then there can be a (B, A, M1)
entry, but there can be no (A, B, M1) entry.
'''

def arbitrage_possible(exchange_rates):
    pass

if __name__ == '__main__':
    import sys
    exchange_rates = []
    this_rate = []
    for idx, value in enumerate(sys.argv[1:]):
        if (idx + 1) % 3:
            this_rate.append(value)
        else:
            this_rate.append(float(value))
            exchange_rates.append(this_rate)
            this_rate = []

    print('currency exchange rates: {}'.format(exchange_rates))
    if arbitrage_possible(exchange_rates):
        print('Arbitrage IS possible.')
    else:
        print('Arbitrage IS NOT possible.')
