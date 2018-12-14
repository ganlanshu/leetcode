# coding=utf-8

"""
用python自己实现heap
"""

class Heap(object):

    def __init__(self):
        # 数据从索引1开始,第0个位置存放0
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, k):
        # 把元素k插入最小堆
        self.heap_list.append(k)
        self.current_size += 1
        self.per_up(self.current_size)

    def perc_up(self, i):
        # 调整第i个元素,使heap_list成为最小堆
        self.heap_list[0] = self.heap_list[i]
        while i//2 > 0 and self.heap_list[0] < self.heap_list[i//2]:
            self.heap_list[i] = self.heap_list[i//2]
            i = i//2
        self.heap_list[i] = self.heap_list[0]

    def del_min(self):
        # 删除最小堆的元素,使剩下的元素还是最小堆
        if self.current_size < 1:
            return
        del_item = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return del_item

    def perc_down(self, i):
        # 删除元素之后,调整元素,使成为最小堆
        while i <= self.current_size//2:
            # 找到左右两个孩子中较小那一个的索引
            if 2*i+1 > self.current_size:
                min_index = 2*i
            else:
                if self.heap_list[2*i] < self.heap_list[2*i+1]:
                    min_index = 2*i
                else:
                    min_index = 2*i+1
            # 从根节点开始调整元素
            if self.heap_list[i] > self.heap_list[min_index]:
                self.heap_list[i], self.heap_list[min_index] = self.heap_list[min_index], self.heap_list[i]
                i = min_index
            else:
                break

    def build_heap(self, alist):
        """
        利用数组alist里的多个元素,组成一个最小堆
        从第一个非叶子节点开始,也就是i//2, 每个节点下沉,把最小值往上浮,直到根节点为止
        :param alist:
        :return:
        """
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        i = len(alist)//2
        while i > 0:
            self.perc_down(i)
            i -= 1


"""
下面的堆索引从0开始
iparent = index
i_left = index*2+1
i_right = index*2+2
"""

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def build_max_heapify(array):
    # 把一个数组变成最大堆
    # 按照数组原样画一个完全二叉树出来,从第一个非叶子节点i开始,以i为根节点,构建max_heap
    n = len(array)
    # 第一个非叶子节点
    i_parent = n//2-1
    while i_parent >= 0:
        max_heapify(array, i_parent, n)
        i_parent -= 1


def max_heapify(array, index, heapsize):
    # 把节点index为根的堆变成最大堆
    while 2*index+1 < heapsize:
        i_left = 2*index+1
        i_right = i_left+1
        if i_right >= heapsize:
            max_index = i_left
        else:
            if array[i_left] < array[i_right]:
                max_index = i_right
            else:
                max_index = i_left
        if array[index] < array[max_index]:
            swap(array, index, max_index)
            index = max_index
        else:
            break


def heap_sort(alist):
    heapsize = len(alist)
    build_max_heapify(alist)
    # 再把alist最后一个元素之外的列表设为最大堆
    for i in range(heapsize-1, 0, -1):
        # 把最大堆的最大值放到alist末尾
        swap(alist, 0, i)
        max_heapify(alist, 0, i)

if __name__ == '__main__':
    alist = [2,3,10,4,20,21,0,-1]
    heap_sort(alist)
    print alist
