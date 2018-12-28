# coding=utf-8
"""
155. Min Stack
Design a stack that supports push, pop, top
and retrieving the minimum element in constant time.
"""

class MinStack(object):
    """
    用2个栈来实现
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        elif x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

class MinStack1(object):
    """
    用一个栈来实现, 入栈的时候存的不是push的元素本身,而是该元素与最小值的差值
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.push(0)
            self.min = x
        else:
            self.stack.push(x-self.min)
            self.min = min(x, self.min)

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min-pop

    def top(self):
        """
        :rtype: int
        """
        if self.stack[-1] < 0:
            return self.min
        else:
            return self.min + self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()