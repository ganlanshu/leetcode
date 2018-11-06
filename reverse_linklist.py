# -*- coding:utf-8 -*-
"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode or not listNode.next:
            return listNode
        pre = None
        while listNode:
            temp = listNode.next
            listNode.next = pre
            pre = listNode
            listNode = temp
        return pre


