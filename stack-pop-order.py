# coding=utf-8

"""
给定一个序列,是栈的入栈顺序,再给定一个序列,判断该序列是不是前一个序列的出栈顺序
"""

class Solution(object):

    def IsPopOrder(self, pushV, popV):
        # write code here
        """
        用一个辅助栈,遍历出栈序列,如果辅助栈顶和出栈序列不一样,
        就把入栈序列的元素进入辅助栈,直到栈顶元素和辅助栈一样,再从辅助栈里出去
        最后如果辅助栈为空,顺序就是对的
        :param pushV:
        :param popV:
        :return:
        """
        if not pushV or not popV:
            return
        help_stack = [pushV[0]]
        push_index = 1
        for pop in popV:
            while pop != help_stack[-1] and push_index < len(pushV):
                help_stack.append(pushV[push_index])
                push_index += 1
            if pop == help_stack[-1]:
                help_stack.pop()
        return True if not help_stack else False

