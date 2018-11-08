#coding=utf-8
"""
Implement Stack using Queues
"""
from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = deque([])


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.value.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        q1 = deque([])
        while len(self.value) > 1:
            q1.append(self.value.popleft())
        top = self.value.popleft()
        self.value = q1
        return top



    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        q1 = deque([])
        while len(self.value) > 1:
            q1.append(self.value.popleft())
        top = self.value[0]
        q1.append(self.value.popleft())
        self.value = q1
        return top


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.value:
            return False
        return True



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
#obj.push(3)
#obj.push(4)
#param_2 = obj.pop()
#obj.pop()
#param_3 = obj.top()
param_4 = obj.empty()
print param_4
#print param_2, param_3, param_4