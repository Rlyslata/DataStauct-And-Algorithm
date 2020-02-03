"""
冒泡排序：
    算法思想：
        未排序的序列，必然存在两个不符合排序规则的相邻元素。
        array 长度 为 n
        一轮排序过程：
            对array[i]，将之array[i+1]比较，并交换他们的值，然后i++，直到i = n-1-i(n-i~n-1是已经排好序的，再参与比较无意义)
        一轮排序结果：
            经过一轮排序后，会将0~n-i-1中的最大值放到后面n-i-1的位置

        (从大到小排序以从n-1~0的顺序执行，每轮排序会将未参与排序的序列中的最小值放到前面）

"""


def bubbleSort(array):
    values = list(array)

    for i in range(0, len(values)):

        for j in range(0, len(values) - i - 1):
            if values[j] > values[j + 1]:
                # 此处j == j+1 恒为假，可以放心使用异或 或 加减排序
                values[j] = values[j] ^ values[j + 1]
                values[j + 1] = values[j] ^ values[j + 1]
                values[j] = values[j] ^ values[j + 1]

    return type(array)(values)


if __name__ == "__main__":
    seq = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    print(set(seq))
    print(bubbleSort(tuple(seq)))
    print(bubbleSort(seq))
