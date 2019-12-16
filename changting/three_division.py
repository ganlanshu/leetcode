# coding=utf-8
import sys
import os
"""
给定数组a,[1,5,9,1,2,3,5] 数组中的元素可以不限次累加，求累加之后，数组中能被3整除的元素最多有多少个
先对每个元素对3求余，结果有被3整除的，余数为1的，余数为2的
累加能被3整除的个数包括
余数为0的
1和2加在一起被3整除的个数等于1和2中个数较小的那个
剩下的1加自己被3整除的个数，和2加自己被3整除的个数
"""


def get_num_divisible_by_3(num_list):

    num_list = [num % 3 for num in num_list]
    # 能被3整除的个数
    num_of_3 = num_list.count(0)

    # 被3整除后余数为1和2的
    r1 = num_list.count(1)
    r2 = num_list.count(2)

    # 1和2加在一起被整除的个数
    a = min(r1, r2)

    # 剩下的1 或者2 自己加自己被整除的个数
    b = abs(r1-r2)//3
    return num_of_3 + a + b


if __name__ == '__main__':
    alist = [1,1,1,1,1,1,1,1,1,1, 2,2,2,2,2]
    print(get_num_divisible_by_3(alist))
    #input_list = sys.stdin.readlines()
    #input_list = [e.strip() for e in input_list]
    #length = len(input_list)
    #result = []
    #for i in range(2, length, 2):
    #    line = input_list[i].split(' ')
    #    line = [int(e) for e in line]
    #    count_of_each_line = get_num_divisible_by_3(line)
    #    result.append(count_of_each_line)
    #result = [str(i) for i in result]
    #print(os.linesep.join(result))
