#coding=utf-8
"""
232. Implement Queue using Stacks

"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # list的行为更像是stack
        self.value = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.value.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        s = []
        while len(self.value) > 1:
            s.append(self.value.pop())
        peek = self.value.pop()
        while s:
            self.value.append(s.pop())
        return peek

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        s = []
        while self.value:
            s.append(self.value.pop())
        p = s[-1]
        while s:
            self.value.append(s.pop())
        return p

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.value == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()