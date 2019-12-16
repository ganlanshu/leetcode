# coding=utf-8

"""
排队接水问题，m个饮水机，最后一个人前面有n个人在排队, n个人每个人接水需要的时间是数组an [1,2,6,28, ...]
求轮到最后一个人接水的时间
"""

import heapq
import sys


def get_wait_time(queue_size, consumer_num, queue_list):
    if queue_size < consumer_num:
        return 1
    if queue_size == consumer_num:
        return min(queue_list)+1

    min_time_heap = queue_list[:consumer_num]
    heapq.heapify(min_time_heap)
    queue_index = consumer_num
    while queue_index < queue_size:
        min_time_heap[0] += queue_list[queue_index]
        heapq.heapify(min_time_heap)
        queue_index += 1
    return min_time_heap[0]+1


if __name__ == '__main__':
    input_list = sys.stdin.readlines()
    num_list = input_list[0].strip().split(' ')
    queue_size, consumer_num = int(num_list[0]), int(num_list[1])
    queue_list = input_list[1].strip().split()
    queue_list = [int(e) for e in queue_list]
    r = get_wait_time(queue_size, consumer_num, queue_list)
    print(r)
