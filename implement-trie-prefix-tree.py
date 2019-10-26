# coding=utf-8
from collections import defaultdict

"""
208. Implement Trie (Prefix Tree)
"""


class Trie(object):

    def __init__(self):
        self.root = {}
        self.end = -1

    def insert(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node[self.end] = True

    def search(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        # check if is end
        return self.end in current_node

    def startswith(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return True

