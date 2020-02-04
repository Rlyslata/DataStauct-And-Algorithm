"""
归并排序：
   和快速排序一样，归并排序也是使用一个分而治之的策略。但归并排序和快速排序不同，归并排序
   选择中间元素为分解点，将序列分成两等份，然后分别递归处理左右两部分。

   算法思想：
    归并排序可分为两部分：
        第一部分为“分”：将序列分成两等份，并分别递归处理他们

        第二部分为“并“：当下层递归结束返回后，我们需要将下层递归处理好的子序列”并“起来，即将两个有序子序列 合并成一个有序序列

        合并完后将序列拷贝到原数组中，然后结束本层递归调用，返回到上一层递归调用，继续执行“并”，直到第一层递归调用也结束，算法结束
"""


# array为原数组，array_tmp为临时数组，array_tmp由调用函数定义，降低程序内存压力
def merge_sort(array, array_tmp, start, end):
    # 递归出口
    if start == end:
        return

    mid_point = (start + end) // 2

    merge_sort(array, array_tmp, start, mid_point)
    merge_sort(array, array_tmp, mid_point + 1, end)

    # 合并子序列start~mid_point,mid_point+1~end
    left_index = start
    right_index = mid_point + 1
    tmp_index = start
    while left_index <= mid_point and right_index <= end:
        if array[left_index] <= array[right_index]:
            array_tmp[tmp_index] = array[left_index]
            left_index = left_index + 1
        else:
            array_tmp[tmp_index] = array[right_index]
            right_index = right_index + 1

        tmp_index = tmp_index + 1

    # 将左右剩余的元素加入array_tmp
    while left_index <= mid_point:
        array_tmp[tmp_index] = array[left_index]
        tmp_index = tmp_index + 1
        left_index = left_index + 1

    while right_index <= end:
        array_tmp[tmp_index] = array[right_index]
        tmp_index = tmp_index + 1
        right_index = right_index + 1

    # 将array_tmp中左右子序列合并成的新的有序序列拷贝回array，供上一层递归调用使用它（作为上一层的子序列）
    for i in range(start, end + 1):
        array[i] = array_tmp[i]


# 调用接口
def mergeSort(array):
    # array_tmp = array会导致二者指向同一对象，合并时出错
    array_tmp = [0] * len(array)
    merge_sort(array, array_tmp, 0, len(array) - 1)


if __name__ == "__main__":
    seq = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 909, 80, 8]
    mergeSort(seq)
    print(seq)
