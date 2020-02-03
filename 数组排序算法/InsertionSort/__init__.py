# 插入排序
"""
    算法思想：
        n为序列长度

        将待排序序列分成两段，一段是已排序序列（初始长度为0），另一段是未排序序列（初始长度为n），
        （若待排序序列不为空，已排序序列长度初始也可以是1，这样可以少执行一次）


        算法每次从未排序序列中取出一个元素，随后找到它在已排序序列中的位置，并将它插入已排序序列
        共执行n次

"""


def insertion_sort(array):
    values = list(array)

    for i in range(1, len(values)):
        """找到value[i] 在 已排序序列values[0]~values[i-1]中的位置，并将之插入"""
        # 从小到大

        # 此处必须要tmp，否则在下面用到value[i]时，会因为value[i]已被改变而出错
        tmp = values[i]

        # j = 0 此处貌似 是PyCharm的问题，显示 j never be used
        for j in range(i - 1, -1, -1):
            if values[j] > tmp:
                values[j + 1] = values[j]
            else:
                values[j + 1] = tmp
                break
        # print(j)
    return type(array)(values)


if __name__ == "__main__":
    seq = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    print(set(seq))
    print(insertion_sort(tuple(seq)))
    print(insertion_sort(seq))
