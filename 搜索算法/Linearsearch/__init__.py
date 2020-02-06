"""

线性搜索：
    线性搜索可以应用于无序或有序序列，对于有序序列当搜索目标不在序列中时可以提前结束搜索，但时间复杂度为O（N）

"""


# array 为从大到小的有序序列
def linear_search(array, target):
    for i in range(0, len(array)):
        if array[i] == target:
            return i
        elif array[i] > target:
            return -1


if __name__ == "__main__":
    seq = [1, 2, 3, 5, 6, 9, 100, 112, 123, 89]
    assert linear_search(seq, 112) != -1, "断言为假"
