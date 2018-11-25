# coding=utf-8

"""
146. LRU Cache
"""
from functools

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.last_visited = []
        self.cache_dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache_dict:
            if key != self.last_visited[-1]:
                self.last_visited.remove(key)
                self.last_visited.append(key)
            return self.cache_dict.get(key)
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache_dict:
            if key != self.last_visited[-1]:
                self.last_visited.remove(key)
                self.last_visited.append(key)
            self.cache_dict[key] = value
        else:
            if len(self.cache_dict) >= self.capacity:
                delete_key = self.last_visited.pop(0)
                del self.cache_dict[delete_key]
            self.last_visited.append(key)
            self.cache_dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict
class LRUCache1(object):
    """
    用ordereddict实现
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cache.has_key(key):
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
