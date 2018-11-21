# coding=utf-8
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):

    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}


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

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = RandomListNode(node.label)
                return self.visited[node]
        return None

    def copyRandomList1(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return head

        old_node = head
        # Creating the new head node.
        new_node = RandomListNode(old_node.label)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]

    def copyRandomList2(self, head):
        """
        把复制节点放在每一个源节点的后面
        然后从头遍历新的链表,取出复制后的部分
        解释参考链接
        https://leetcode.com/problems/copy-list-with-random-pointer/solution/
        :param head:
        :return:
        """
        if not head:
            return
        current = head
        # 复制原链表的每个节点,形成 A->A'->B->B'->C->C'
        while current:
            post = current.next
            current_copy = RandomListNode(current.label)
            current.next = current_copy
            current_copy.next = post
            current = post

        # 修改复制节点的random指针,改为源节点的random指针的复制节点
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # 从head链表里挑出复制出来的新节点
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new
