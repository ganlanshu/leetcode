# coding=utf-8
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        node_copy_dict = {}
        current = head
        dummy = RandomListNode(0)
        head_copy = RandomListNode(head.label)
        node_copy_dict[head] = head_copy
        dummy.next = head_copy
        pre = dummy

        while current:
            if current not in node_copy_dict:
                current_copy = RandomListNode(current.label)
                node_copy_dict[current] = current_copy
            else:
                current_copy = node_copy_dict[current]
            random = current.random
            if random:
                if random not in node_copy_dict:
                    random_copy = RandomListNode(random.label)
                    node_copy_dict[random] = random_copy
                else:
                    random_copy = node_copy_dict.get(random)
                current_copy.random = random_copy
            after = current.next
            if after:
                if after not in node_copy_dict:
                    after_copy = RandomListNode(after.label)
                    node_copy_dict[after] = after_copy
                else:
                    after_copy = node_copy_dict.get(after)
                current_copy.next = after_copy
            current = after
        return dummy.next
