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
