"""
二分搜索：
    只适用于有序序列array（以从小到大为例）
    采用渐进的策略，将范围逐渐缩小，若带搜索序列起始下标为min，最后一个元素下标为max
    首次检查mid = (min+max)/2 位置的元素是否为搜索目标target，
    if array[mid]==target,则表示寻到目标
    if array[mid]>target,则目标在min~mid中，将max更新为mid继续执行算法
    if array[mid]<target,则目标在mid~max中，将max更新为mid继续执行算法
"""


def binary_search(array, target):
    min_ = 0
    max_ = len(array) - 1
    while min_ <= max_:
        mid = (min_ + max_) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            max_ = mid-1
        else:
            min_ = mid+1

    return -1


if __name__ == "__main__":
    seq = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    assert binary_search(seq, 2) == 1, "未找到"
