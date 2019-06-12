'''
March 26, 2019

Given an unordered list of flights taken by someone, each represented as
(origin, destination) pairs, and a starting airport, compute the person's
itinerary. If no such itinerary exists, return null. If there are multiple
possible itineraries, return the lexicographically smallest one. All flights
must be used in the itinerary.

For example, given the list of flights
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL', you should return the list
['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport
'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and
starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even
though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first
one is lexicographically smaller.
'''

def get_itinerary(flights, starting_airport):
    flights.sort()
    return _get_itinerary(flights, starting_airport, starting_airport)

def _get_itinerary(flights, starting_airport, itinerary):
    if not flights:
        return itinerary

    for idx, (start, end) in enumerate(flights):
        if start == starting_airport:
            result = _get_itinerary(
                flights[:idx] + flights[idx + 1:],
                end,
                itinerary + ' -> ' + end
            )
            if result:
                return result

def parse_inputs(inputs):
    flights = [
        (inputs[idx], inputs[idx + 1])
        for idx in range(0, len(inputs) - 1, 2)
    ]
    starting_airport = inputs[-1]
    return flights, starting_airport

if __name__ == '__main__':
    import sys
    flights, starting_airport = parse_inputs(sys.argv[1:])
    print('flights: {}'.format(flights))
    print('starting airport: {}'.format(starting_airport))
    print('itinerary: {}'.format(get_itinerary(flights, starting_airport)))