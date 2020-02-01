# 链表节点类
class Node:
    def __init__(self, value, Next):
        self.value = value
        self.next = Next


# 链表类
class LinkedList(Node):
    # 初始化链表
    def __init__(self):
        super(LinkedList, self).__init__(0, None)
        self.size = 0
        # 尾指针、头指针（哨兵）
        self.tail = self.sentinel = Node(value=self.value, Next=None)

    # 尾部追加
    def append_(self, value):
        self.tail.next = Node(value=value, Next=None)
        self.tail = self.tail.next
        self.size += 1

    # 打印函数
    def __str__(self):
        cell = self.sentinel.next
        while cell:
            print(cell.value)
            cell = cell.next

    def hasLoopMark(self):
        # 采用标记单元格的方式来 判断是否有环
        """
        在Node中多加一个数据域 visited

        算法执行过程：
            从sentinel开始访问链表每一个节点，判断节点visited是否为True，
            若是，则说明链表存在环，node.next = None 破环
            时间复杂度 = O(N)
            空间复杂度 = N
        :return: boolean

        """

        pass

    def hasLoopHashTable(self) -> bool:
        # 使用哈希表（散列表）
        """
        定义一个哈希表，哈希表的大小应为 1.5*link.size
        算法执行过程：
            从sentinel开始访问每一个节点，检查是否哈希表是否已存在该节点，若存在则存在环，
            返回True，否则，将该节点加入哈希表
        时间复杂度 = O(N)
        空间复杂度 = N
        :return:bool
        """
        pass

    def hasLoopLinkRetracing(self):
        # 链表回溯法
        """
        使用两个Node对象，遍历链表，当两个对象不相等，且next一致时，说明检测到了环
        时间复杂度 = O(N**2)
        空间复杂度 = 1
        :param self:
        :return:
        """
        node_ = self.sentinel
        while node_.next:
            # node不断往前推进，对每个node，tracer都从sentinel开始检测，直到与node相遇或检测到环结束算法
            tracer = self.sentinel
            while tracer != node_:
                if tracer.next == node_.next:
                    node_.next = None
                    return True
                tracer = tracer.next
            node_ = node_.next

    # 反转链表
    def reverseList(self):
        pre_node = None
        curr_node = self.sentinel.next

        while curr_node:
            next_node = curr_node.next
            curr_node.next = pre_node
            pre_node = curr_node
            curr_node = next_node

        self.sentinel.next = pre_node


if __name__ == "__main__":
    # 初始空链表
    link = LinkedList()
    # 制造循环链表
    # 循环开始节点
    start = None
    for i in range(0, 9):
        if i == 4:
            start = link.tail
        link.append_(i)
    # 设置·循环
    link.tail.next = start

    # 测试部分

    # expect output ：9
    print("link.size=" + str(link.size))

    # expect output ：True
    print(link.hasLoopLinkRetracing())

    # expect output ：[0,...,8]
    link.__str__()

    # expect output: [8,...,0]
    link.reverseList()
    # link.reverseList()
    link.__str__()
