# coding=utf-8

import os
import sys


def get_first_gte(target, sorted_list):
    start = 0
    end = len(sorted_list)-1
    while start <= end:
        mid = (start+end)//2
        if sorted_list[mid] < target:
            start += 1
        else:
            end = mid-1
    if end == len(sorted_list)-1:
        return len(sorted_list)-1
    return end+1


def get_last_lte(target, sorted_list):
    start = 0
    end = len(sorted_list)-1
    while start <= end:
        mid = (start+end)//2
        if sorted_list[mid] <= target:
            start = mid+1
        else:
            end = mid-1
    if start == 0:
        return len(sorted_list)-1
    return start-1


def get_count_in_scope(start_value, end_value, sorted_list):
    """
    找到有序数组sorted_value在start_value 和end_value之间元素的个数，包含起始值
    :param start_value:
    :param end_value:
    :param sorted_list:
    :return:
    """
    low = 0
    high = len(sorted_list)-1
    while low <= high:
        mid = (low + high)//2
        if sorted_list[mid] > start_value:

    return high-low+1


def main(input_list):
#def main(input_list):
    #input_list = input_str.split(os.linesep)
    #print(input_list)
    # 所有分组的个数
    input_list = [l.strip() for l in input_list]
    group_count = int(input_list[0])

    result = []
    lines_passed = 1
    for group_id in range(group_count):
        group_start_index = lines_passed
        timestamp_inner_group = []
        timestamp_count_inner_group = int(input_list[group_start_index])
        index = group_start_index + 1
        timestamp_end_index = index + timestamp_count_inner_group

        while index < timestamp_end_index:
            timestamp_inner_group.append(int(input_list[index]))
            index += 1

        # 对一组内的时间戳排序
        timestamp_inner_group.sort()
        scope_line_count = int(input_list[index])
        index += 1
        scope_end_index = index + scope_line_count
        while index < scope_end_index:
            line = input_list[index].split(' ')
            start_value, end_value = int(line[0]), int(line[1])
            count_between_scope = get_count_in_scope(start_value, end_value, timestamp_inner_group)
            result.append(count_between_scope)
            index += 1
        lines_passed += timestamp_count_inner_group + scope_line_count + 1 + 1

    return os.linesep.join([str(i) for i in result])


if __name__ == '__main__':
    input_list = sys.stdin.readlines()
    print(main(input_list))


a = """
1
5
1564900000
1564900005
1564900008
1564900007
1564900009
5
0 9999999999
1564900008 1564900008
1564900006 1564900006
1564900007 1564900009
1564900000 1564900007
"""
