"""
选择排序：
        算法思想：
            假设 array 长度为 n

            对array[i]，算法寻找出 序列{array[j>=i]} 的最小值（从小到大）array[j]
            交换array[i] 与array[j]

"""


def selection_sort(array):
    values = list(array)
    for i in range(0, len(values)):

        # 寻找最小值min_
        min_ = i
        for j in range(i, len(values)):
            if values[min_] > values[j]:
                min_ = j

        # 交换值
        a = values[min_]
        b = values[i]
        values[min_] = b
        values[i] = a

        # 使用异或或加减法，交换数组元素值时要特别注意，当min_==i时，下一步使用的值已经变了，导致结果错误，下面的就是如此：
        # values[min_] = values[min_] ^ values[i]
        # values[i] = values[min_] ^ values[i]
        # values[min_] = values[min_] ^ values[i]
        """
        原理：a^0 == a, 0 == a^a
        相似的还有加交换：
        a = a+b
        b = a-b
        a = a-b
        """

    return type(array)(values)


if __name__ == "__main__":
    seq = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(selection_sort(seq))
