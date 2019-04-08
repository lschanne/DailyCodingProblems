'''
April 6, 2019

Implement an LRU (Least Recently Used) cache. It should be able to be
initialized with a cache size n, and contain the following methods:
 - set(key, value): sets key to value. If there are already n items in the
   cache and we are adding a new item, then it should also remove the least
   recently used item.
 - get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
'''

class LRU_item:
    def __init__(self, key, prev_item=None, next_item=None):
        self.key = key
        self.prev_item = prev_item
        self.next_item = next_item

# It ended up being a surprising amount of code to implement this LRU. I wonder
# what I could have done better
class LRU:
    def __init__(self, n):
        if n <= 0:
            raise ValueError('n must be a positive integer!')
        self.n = n
        self._cache = {}
        self._least_recently_used = None
        self._most_recently_used = None
        self._count = 0

    def set(self, key, value):
        if key in self._cache:
            _, lru_item = self._cache[key]
            self._touch_item(lru_item)
        else:
            lru_item = self._add_to_lru(key)
            if self._count > self.n:
                self._pop_lru()

        self._cache[key] = (value, lru_item)

    def get(self, key):
        if key in self._cache:
            value, lru_item = self._cache[key]
            self._touch_item(lru_item)
            return value

    def _touch_item(self, lru_item):
        if self.n == 1:
            return

        if lru_item.next_item and lru_item.prev_item:
            lru_item.next_item.prev_item = lru_item.prev_item
            lru_item.prev_item.next_item = lru_item.next_item
        elif lru_item.next_item:
            # the item is already the most recent; do nothing
            return
        elif lru_item.prev_item:
            # the item is the least recent
            self._least_recently_used = lru_item.prev_item
            self._least_recently_used.next_item = None

        lru_item.prev_item = None
        if self._most_recently_used:
            lru_item.next_item = self._most_recently_used
            self._most_recently_used.prev_item = lru_item
        else:
            lru_item.next_item = self._least_recently_used
            self._least_recently_used.prev_item = lru_item

        self._most_recently_used = lru_item

    def _add_to_lru(self, key):
        self._count += 1
        lru_item = LRU_item(key)
        if not self._least_recently_used:
            self._least_recently_used = lru_item
        elif not self._most_recently_used:
            self._most_recently_used = lru_item
            self._least_recently_used.prev_item = self._most_recently_used
            self._most_recently_used.prev_item = self._least_recently_used
        else:
            lru_item.next_item = self._most_recently_used
            self._most_recently_used.prev_item = lru_item
            self._most_recently_used = lru_item

        return lru_item

    def _pop_lru(self):
        self._count -= 1
        key = self._least_recently_used.key
        if self._least_recently_used.prev_item:
            self._least_recently_used = self._least_recently_used.prev_item
            self._least_recently_used.next_item = None

        if self._least_recently_used.key == self._most_recently_used.key:
            self._most_recently_used = None

        del self._cache[key]

# I tested this one more interactively using IPython