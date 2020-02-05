"""
计数排序：
    已知待排序序列数据范围0~max_value,用一个大小为max_value+1的数组count记录各个数据的个数，
    最后依据数组count将数据填充到待排序序列

    若待排序序列大小为N,count大小为M，
    在排序算法中，需要花费M步初始化count, N步遍历待排序序列得到count数组，
    最后需要花费N步填充待排序序列
    因此计数排序总步数为2*N+M，时间复杂度为O(N)

"""


def counting_sort(array, max_value):
    # 初始化count
    count = [0] * (max_value+1)

    # 计数
    for i in range(0,len(array)):
        count[array[i]] += 1

    # 填充array
    index = 0
    for i in range(0,max_value+1):
        for j in range(0,count[i]):
            array[index] = i
            index += 1


if __name__ == "__main__":
    seq = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    counting_sort(seq,6)
    print(seq)