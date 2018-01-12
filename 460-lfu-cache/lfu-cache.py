# -*- coding:utf-8 -*-


# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
#
#
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
#
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LFUCache cache = new LFUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
#


class LFUCache(object):
    def __init__(self, capacity):
        self.remain = capacity
        self.nodesForFrequency = collections.defaultdict(collections.OrderedDict)
        self.leastFrequency = 1
        self.nodeForKey = {}

    def _update(self, key, newValue=None):
        value, freq = self.nodeForKey[key]
        if newValue is not None: value = newValue
        self.nodesForFrequency[freq].pop(key)
        if len(self.nodesForFrequency[self.leastFrequency]) == 0: self.leastFrequency += 1
        self.nodesForFrequency[freq+1][key] = (value, freq+1)
        self.nodeForKey[key] = (value, freq+1)

    def get(self, key):
        if key not in self.nodeForKey: return -1
        self._update(key)
        return self.nodeForKey[key][0]

    def put(self, key, value):
        if key in self.nodeForKey: self._update(key, value)
        else:
            self.nodeForKey[key] = (value,1)
            self.nodesForFrequency[1][key] = (value,1)
            if self.remain == 0:
                removed = self.nodesForFrequency[self.leastFrequency].popitem(last=False)
                self.nodeForKey.pop(removed[0])
            else: self.remain -= 1
            self.leastFrequency = 1 # should be one after adding a new item


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
