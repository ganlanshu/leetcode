# coding=utf-8

"""
146. LRU Cache
"""
from collections import deque

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