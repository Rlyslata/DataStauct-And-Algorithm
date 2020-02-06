"""
插值搜索：
    与二分搜索类似但在取mid的方式上不同，插值搜索mid = min +(max-min)*(target -array[min])/(array[max]-array[min]),
    意思是：根据target与array[min],及与array[max]距离之比来预测下标
    插值搜索对于分布相当均匀的序列时间复杂度可达到O(log(logN)),最糟糕的情况下也有O(N)(数据分布随机性很强，或者说跳度很大)

"""


def interjection_search(array, target):
    min_ = 0
    max_ = len(array) - 1
    while min_ <= max_:
        # 检查是否还在搜索范围内
        if target < array[min_] or target > array[max_]:
            return -1
        mid = min_ + (max_ - min_) * (target - array[min_]) // (array[max_] - array[min_])
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            max_ = mid - 1
        else:
            min_ = mid + 1
    return -1


if __name__ == "__main__":
    seq = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    assert interjection_search(seq, 3) == -1, "未找到"
