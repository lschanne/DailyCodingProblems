'''
May 21, 2019

Write a map implementation with a get function that lets you retrieve the value
of a key at a particular time.

It should contain the following methods:
- set(key, value, time): sets key to value for t = time.
- get(key, time): gets the key at t = time.
The map should work like this. If we set a key at a particular time, it will
maintain that value forever or until it gets set at a later time. In other
words, when we get a key at a time, it should return the value that was set for
that key set at the most recent time.

Consider the following examples:
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2
d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
'''

class TimeMap:
    def __init__(self):
        self.mapp = {}

    def set(self, key, value, time):
        if key not in self.mapp:
            self.mapp[key] = {}
        self.mapp[key][time] = value

    def get(self, key, time):
        time_mapp = self.mapp.get(key)
        if time_mapp is None:
            return None

        most_recent_value = None
        most_recent_time = -1 # assuming all times are positive
        for this_time, this_value in time_mapp.items():
            if this_time <= time and this_time > most_recent_time:
                most_recent_time = this_time
                most_recent_value = this_value

        return most_recent_value

if __name__ == '__main__':
    d = TimeMap()
    d.set(1, 1, 0) # set key 1 to value 1 at time 0
    d.set(1, 2, 2) # set key 1 to value 2 at time 2
    r = d.get(1, 1) # get key 1 at time 1 should be 1
    print(r, 1)
    r = d.get(1, 3) # get key 1 at time 3 should be 2
    print(r, 2)
    d.set(1, 1, 5) # set key 1 to value 1 at time 5

    #### So this next line that was given as a requirement is not right
    #### the first thing we do is set key 1 at time 0 to be 1
    #### I am also not seeing in the spec anything that would nullify that
    #### Therefore, I believe that this d.get(1, 0) should return 1, which it
    #### does
    r = d.get(1, 0) # get key 1 at time 0 should be null
    print(r, None)

    r = d.get(1, 10) # get key 1 at time 10 should be 1
    print(r, 1)
    d.set(1, 1, 0) # set key 1 to value 1 at time 0
    d.set(1, 2, 0) # set key 1 to value 2 at time 0
    r = d.get(1, 0) # get key 1 at time 0 should be 2
    print(r, 2)
