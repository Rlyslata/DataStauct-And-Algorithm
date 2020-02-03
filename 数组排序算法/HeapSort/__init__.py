"""
堆排序：
    堆的定义与特性：
            堆是一颗空树或有序的完全二叉树（完全二叉树即叶子节点只出现在最后两层，且除了最后一层，其它层都是节点数量都是2**h个），堆（最大堆）的任意节点值都大于其子节点值。

            堆分为最大堆和最小堆：
                最大堆：任意节点值大于其子节点值，根节点为最大值
                最小堆：任意节点值小于其子节点值，根节点为最小值

            第i个节点的左、右子节点下标分别为2*i+1,2*i+2, 其父节点下标为(i-1)/2

    调整堆：
        下滤：从根节点开始，比较当前节点与其子节点的大小，若子节点值大于它，则要把它与其子节点交换。重复该操作直到叶子节点

        上滤：从最后一个节点开始（最后一层的最后一个节点），比较当前节点与其父节点的值得大小，若父节点值小于它，则将其余父节点交换，
        重复操作直到根节点

    算法思想（最大堆）:

        1.建立堆（最大堆）
            对于数组heap[n]，从heap[1]（根节点的子节点）开始，检查heap[i] （n>i>=1）是否 不大于 heap[(i-1)/2], 若大于，则需交换他们的值 。
            heap[n-1]调整完毕后，最大堆建立完成
        2.维护堆
            删除堆顶：
                删除堆顶，不是说从堆顶删除，堆的删除和添加元素都是在堆尾部进行的，目的是为了便于维护堆这个数据结构。删除堆顶是指将根节点与最后一个节点交换，进而删除最后一个节点。
                将最后一个节点放置堆顶后，heap不再是堆，需要从堆顶开始调整，即下滤。

            添加元素：同样添加元素也只能在堆尾进行，添加元素后，需要重新从堆新加元素开始调整，即上滤。

        堆排序，实际就是建立堆、维护堆或者说添加元素、删除堆顶的过程。
"""


class Heap:
    def __init__(self, array):
        self.max_heap = self.min_heap = array
        self.size = len(array)

    def up_filter(self, start):
        # 从start开始上滤
        while start != 0:
            parent = (start - 1) // 2
            if self.max_heap[parent] < self.max_heap[start]:
                tmp = self.max_heap[parent]
                self.max_heap[parent] = self.max_heap[start]
                self.max_heap[start] = tmp
            else:
                # 维护完成
                break
            start = parent

    def down_filter(self, start=0):
        # 从start开始下滤
        while start < self.size:
            child_left = start * 2 + 1
            child_right = start * 2 + 2

            # 若没有子节点，标记为父节点
            if child_left >= self.size:
                # global child_left
                child_left = start
            if child_right >= self.size:
                # global child_right
                child_right = start

            # 维护完成
            if self.max_heap[child_right] <= self.max_heap[start] and self.max_heap[child_left] <= self.max_heap[start]:
                break

            child_max = child_left if self.max_heap[child_left] >= self.max_heap[child_right] else child_right

            # 与最大的子节点交换
            tmp = self.max_heap[child_max]
            self.max_heap[child_max] = self.max_heap[start]
            self.max_heap[start] = tmp

            # start下滤完成，继续跟踪其子节点
            start = child_max

    def make_max_heap(self):
        # 将一个数组调整为最大堆，下面的代码意思是，想一个空堆中逐渐加入array中的元素，
        # 也就是说要进行添加元素操作，即上滤，待将array中元素全部加入堆后，最终形成最大堆。
        for curr_node in range(0, self.size):
            self.up_filter(curr_node)
        return self

    def remove_root(self):
        # 删除堆顶
        if self.size == 0:
            # 堆为空不能删除
            raise IndexError("堆空了")
        ret = self.max_heap[0]
        # 交换堆顶与堆尾元素
        if self.size > 1:
            self.max_heap[0] = self.max_heap[0] ^ self.max_heap[self.size - 1]
            self.max_heap[self.size - 1] = self.max_heap[0] ^ self.max_heap[self.size - 1]
            self.max_heap[0] = self.max_heap[0] ^ self.max_heap[self.size - 1]
        self.size = self.size - 1

        # 调整最大堆，下滤
        self.down_filter(start=0)

        return ret

    def heap_sort(self):
        ret = []
        while True:
            try:
                ret.append(self.remove_root())
            except IndexError:
                break
        return ret


if __name__ == "__main__":
    array_ = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    max_heap = Heap(array_).make_max_heap()
    print(max_heap.max_heap)
    print(max_heap.heap_sort())

