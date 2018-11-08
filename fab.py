#coding=utf-8

def fibonacci(n):
    """
    最简单的先用递归
    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_with_iter(n):
    """
    每次递归没有存下来之前已经算出来的结果,浪费很多次计算,下面把每次的结果存在一个列表里
    :param n:
    :return:
    """
    result = []
    result.append(0)
    result.append(1)
    if n >= 2:
        for i in range(2, n+1):
            result.append(result[i-1] + result[i-2])
    return result

def fibonacci3(n):
    """
    第二种做法把每一次计算的结果都存下来,占用了较多的空间,其实只需要存当前节点的前面两个节点就够了
    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0, f1 = 0, 1
    for i in range(2, n+1):
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return fn

if __name__ == '__main__':
    print fibonacci3(10)
    print fibonacci_with_iter(10)