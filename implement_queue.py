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
        if not self.value:
            return
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


class MyQueue1(object):
    """
    看了讨论区其他解法，觉得初始化用2个栈更方便，如果有连续的pop操作效率更高，不需要重新push到原来的栈
    """

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        self.peek()
        return self.stack2.pop()

    def peek(self):
        if self.empty():
            return
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and self.stack2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()