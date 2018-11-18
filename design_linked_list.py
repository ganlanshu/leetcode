#coding=utf-8
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        if not current:
            return -1
        for i in range(index):
            current = current.next
        return current.val



    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = ListNode(val)
        temp = self.head
        node.next = temp
        self.head = node
        self.size += 1




    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = ListNode(val)
        current = self.head
        if not current:
            self.head = node
        else:
            while current:
                pre = current
                current = current.next
            pre.next = node
        self.size += 1



    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        size = self.size
        if index < 0 or index > size:
            return
        if index == 0:
            return self.addAtTail(val)
        current = self.head
        for i in range(index-1):
            current = current.next
        node = ListNode(val)
        temp = current.next
        node.next = temp
        current.next = node
        self.size += 1


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        size = self.size
        if index < 0 or index >= size:
            return
        current = self.head
        if not current:
            return
        if index == 0:
            self.head = current.next
        else:
            for i in range(index):
                pre = current
                current = current.next
            pre.next = current.next
        self.size -= 1

    def addAtIndex1(self, index, val):
        """
        写一个通用的,给头插和尾插方法用
        :param index:
        :param val:
        :return:
        """
        if index < 0 or index > self.size:
            return
        node = ListNode(val)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            node.next = current.next
            current.next = node
        self.size += 1

    def addAtHead1(self, val):
        return self.addAtIndex1(0, val)

    def addAtTail1(self, val):
        size = self.size
        return self.addAtIndex1(size, val)



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)