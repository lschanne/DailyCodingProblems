'''
April 21, 2019

Implement an LFU (Least Frequently Used) cache. It should be able to be
initialized with a cache size n, and contain the following methods:
    - set(key, value): sets key to value. If there are already n items in the
                       cache and we are adding a new item, then it should also
                       remove the least frequently used item. If there is a
                       tie, then the least recently used key should be removed.
    - get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''

# Note to self: this is pretty much garbage. It isn't O(1) and I suspect that
# it would definitely have issues in the case of a tie occuring after the
# least frequently used item has been removed
# That being said, this problem isn't very sexy... "maybe I'll come back to it"
class LFU_cache:
    def __init__(self, n):
        self.size = n
        self._count = 0
        self._cache = {}
        self._least_frequently_used = None

    def set(self, key, value):
        if key in self._cache:
            _, count = self._cache[key]
            count += 1
            self._update_lfu_item(key)
        else:
            count = 1
            self._count += 1
            self._pop_lfu_item()

        self._cache[key] = (value, count)

    def get(self, key):
        if key in self._cache:
            value, count = self._cache[key]
            count += 1
            self._cache[key] = (value, count)
            self._update_lfu_item(key)
            return value

    def _pop_lfu_item(self):
        while self._count > self.size:
            self._least_frequently_used = self._get_lfu()
            del self._cache[self._least_frequently_used]
            self._count -= 1

    def _get_lfu(self):
        if self._least_frequently_used is not None:
            lfu = self._least_frequently_used
        elif self._count:
            # Obviously this is not O(1)
            lfu = min(
                self._cache.keys(), key=lambda key: self._cache[key][1]
            )
        else:
            lfu = None
        return lfu

    def _update_lfu_item(self, key):
        if self._least_frequently_used is None:
            self._least_frequently_used = key
        elif self._least_frequently_used == key:
            self._least_frequently_used = None
            self._least_frequently_used = self._get_lfu()