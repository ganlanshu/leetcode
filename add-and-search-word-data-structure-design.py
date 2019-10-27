# coding=utf-8
"""
211. Add and Search Word - Data structure design
"""


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.end = '$'

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.trie
        for letter in word + self.end:
            node = node.setdefault(letter, {})

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def find(word, node):
            if not word:
                return self.end in node
            char, word = word[0], word[1:]
            if char != '.':
                return char in node and find(word, node[char])
            return any(find(word, child) for child in node.values() if child)
        return find(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:


obj = WordDictionary()
obj.addWord('love')
obj.addWord('bad')
obj.addWord('dad')
print(obj.search('love'))
