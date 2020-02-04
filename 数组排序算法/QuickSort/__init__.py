"""
    快速排序：
        快速排序是一种不稳定的排序，与堆排序相比，它也有这O(NlogN)预期的性能，但最坏的情况时间复杂度会上升到O(N**2).

        算法思想：
            每次选择一个分界值divider，将小于divider的放置在序列左边，大于等于divider的放置在右边，
            然后再分别递归解决左边，和右边

        最佳的情况：每次选择的divider都处于序列中间，递归解决，我们可以发现递归树的每层的单个节点中的子序列长度在以2的指数幂递减，
                    最终形成的递归树的深度是logN,而每层总的元素数总是N，故每层需要处理的元素数为N-有限个divider数，N很大时可忽略不计，因此
                    每层需处理的元素数粗略视为N，而递归树层数为logN，故最佳时间复杂度为O(NlogN)

        最坏的情况：每次选择的的divider都是极限值（最大或最小值），导致左边或右边为空。
                    递归结果：若第一层（次）需要递归处理元素数为N，那么接下来调用递归处理左边和右边，需要处理的元素数为N-1，
                    再下一层是N-2，.....1 ,0，这样递归深度就达到了N的层次，整个递归树处理元素个数为N+N-1+...+1 =(N+1)N/2,
                    即时间复杂度达到O(N**2)

        合理的选择分界值：面对几十亿的数据，logN 大约是30，比N小得多，因此分界值divider需要合理的选择，否则很容易达到O(N**2)，
                        更重要的是会导致耗尽堆栈空间，导致程序崩溃。
                       *** 选择第一个元素作为divider
                            当数组本身有序时，或部分有序时，效果不佳
                       *** 在排序之前，将数组随机排列，随机排列使用线型同余发生器，时间复杂度为O(N)
                             当数组size很大时，会消耗一定时间
                       *** 比较首、中间、末三个元素，以他们的中位数作为分界值
                            避免了取极值的情况，但无法避免靠近极值
                       *** 随机待处理序列中的一个值作为分界值
                            犹豫随机性，很难遇到最坏情况


"""


def quick_sort(array, start, end):
    # 没有或只有一个元素直接结束
    if start < 0 or start >= end:
        return

    # 选取第一个作为divider
    divider = array[start]
    low = start
    high = end
    # 把小值放在左边，大值放在右边，起始空位是divider==start，
    # end从右往左扫描，直到遇到low。碰到小于divider的值，将之放置到low，此时空位为end
    # low从左往右扫描，直到遇到end。碰到大于divider的值，将之放置到end的位置，此时空位为low
    # 扫描结束后，将divider放置到low位置，使之处于“中间”位置
    # 递归解决左边（start,low-1),(low+1，end）
    while low < high:
        # end从右往左扫描，直到遇到low。
        while array[high] >= divider:
            high = high - 1
            if low >= high:
                high = low
                break
        array[low] = array[high]

        # 扫描结束
        if low >= high:
            array[low] = divider
            break

        while array[low] < divider:
            low = low + 1
            if low >= high:
                low = high
                break
        array[high] = array[low]

        # 扫描结束
        if low >= high:
            array[low] = divider
            break

    # 递归解决左边
    quick_sort(array, start, low - 1)
    # 递归解决左边
    quick_sort(array, low + 1, end)


if __name__ == "__main__":
    seq = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    quick_sort(seq, 0, len(seq)-1)
    print(seq)
