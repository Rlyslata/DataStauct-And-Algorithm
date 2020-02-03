# 栈

import CircularLinkedList


class EmptyError(Exception):
    def __init__(self, message, expression=__name__):
        # super(EmptyError, self).__init__(message, expression)，此处无需重写
        self.message = message
        self.expression = expression


class Stack(CircularLinkedList.LinkedList):
    def __init__(self):
        super(Stack, self).__init__()

    def push(self, value):
        # 链表栈 无需考虑栈满，直接push
        new_node = CircularLinkedList.Node(value=value)
        new_node.next = self.sentinel.next
        self.sentinel.next = new_node

    def pop(self):
        if self.sentinel.next:
            delete = self.sentinel.next
            self.sentinel.next = delete.next
            return delete.value
        raise EmptyError("栈空，不能pop()")

    """
    栈的应用：
        *逆置数组
        *插入排序
        *选择排序
    """

    @staticmethod
    def reverseArray(array):
        """
        :function：逆置数组
        :param array: 可迭代对象
        :return:

        将数组元素全部入栈，然后再一次出栈，得到逆序的数组
        """
        stack_ = Stack()
        for element in iter(array):
            # list : array.pop()未指定参数，默认抛出最后一项
            stack_.push(element)

        ret = []
        while True:
            try:
                ret.append(stack_.pop())
            except EmptyError as ee:
                break
        del stack_
        # 保持类型不变
        return type(array)(ret)

    @staticmethod
    def insertSort(array):
        """
        插入排序：
            设置两个栈，数据栈：stack_,临时栈：stack_tmp
            元素个数：
            num_items = len(array)
            即将参与排序的元素
            next_item = stack_.pop()

            排序过程：
                将num_items-i-1个未排序的元素从stack_挪到stack_tmp
                再比较next_item 与stack_栈顶元素的大小，比next_item大则挪出（从大到小排序），否则将next_item压入栈stack_中
                最后，将stack_tmp中的元素挪回stack_

                重复上述过程，直到num_items个元素都参与了排序

        :param array:
        :return:
        """
        stack_ = Stack()
        stack_tmp = Stack()
        num_items = len(array)
        if 2 > num_items:
            return array
        # 将array元素倒入stack_
        for it in iter(array):
            stack_.push(it)

        # 插入排序
        for i in range(0, num_items):
            try:
                next_item = stack_.pop()
            except EmptyError as ee:
                # 栈空直接退出
                break

            # 将num_items-1-i个未排序元素挪到stack_tmp
            for j in range(0, num_items - i - 1):
                stack_tmp.push(stack_.pop())

            # 将stack_已排好序的与next_item比较大小
            for k in range(0, i):
                try:
                    tmp = stack_.pop()
                except EmptyError as ee:
                    # 栈空直接退出
                    break
                if tmp > next_item:
                    stack_tmp.push(tmp)
                else:
                    # 放回stack_
                    stack_.push(tmp)
                    break
            # 把next_item 放入stack_
            stack_.push(next_item)
            # 把stack_tmp 中元素挪回stack_
            while True:
                try:
                    stack_.push(stack_tmp.pop())
                except EmptyError as ee:
                    break
            # next_item排序完成

        ret = []
        while True:
            try:
                ret.append(stack_.pop())
            except EmptyError:
                break
        return type(array)(ret)
        pass

    @staticmethod
    def selectSort(array):
        """
        选择排序：
             设置两个栈，数据栈：stack_,临时栈：stack_tmp
            元素个数：
            num_items = len(array)
            即将参与排序的元素
            min of 未排序的元素

            排序过程：
                将num_items-i个未排序的元素从stack_挪到stack_tmp，并比较出他们中的最小值min
                再将min压入stack_
                最后，将stack_tmp中的元素挪回stack_

                重复上述过程，直到num_items个元素都参与了排序
        :param array:
        :return:
        """
        stack_ = Stack()
        stack_tmp = Stack()
        num_items = len(array)

        if 2 > num_items:
            return array
        # 将array元素倒入stack_
        for it in iter(array):
            stack_.push(it)

        # 选择排序
        for i in range(0, num_items):
            min_ = float('inf')
            """
                float('+inf')、float('-inf')表示正、负无穷大
                float('nan')表示NaN
                
                math.isinf、math.isnan可以判断inf与nan
                
                inf与inf运算结果为nan
                
                nan与任何对象比较结果都是false
            """
            # 将num_items-i个未排序元素挪到stack_tmp
            for j in range(0, num_items - i):
                tmp = stack_.pop()
                if tmp < min_:
                    min_ = tmp
                stack_tmp.push(tmp)

            # 把min_ 放入stack_
            stack_.push(min_)

            # 把stack_tmp 中元素挪回stack_,当遇到min_时应跳过
            # 设置skipped是为了防止多次跳过相同的值，若没有skipped当有n>=3个值时，会跳过大于1个
            skipped = False
            while True:
                try:
                    tmp = stack_tmp.pop()
                    if not skipped and tmp == min_:
                        # 遇到min_时应跳过
                        tmp = stack_.pop()
                        stack_.push(stack_tmp.pop())
                        skipped = True
                    else:
                        stack_.push(tmp)
                except EmptyError as ee:
                    break

            # next_item排序完成

        ret = []
        while True:
            try:
                ret.append(stack_.pop())
            except EmptyError as e:
                break
        return type(array)(ret)
        pass


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    print(stack.pop())

    """测试逆置数组"""
    print("""测试逆置数组""")
    a = [1, 2, 3]
    a_ = Stack.reverseArray(a)
    print(str(a_) + "     " + str(type(a_)))

    b = (1, 2, "3")
    b_ = Stack.reverseArray(b)
    print(str(b_) + "     " + str(type(b_)))

    c = "python"
    c_ = Stack.reverseArray(c)
    print(str(c_) + "     " + str(type(c_)))

    """测试插入排序"""
    print("""测试插入排序""")
    array = [1, 3, 5, 2, 10, 3, 2, 7, 19]
    print(Stack.insertSort(array))
    print(Stack.insertSort(tuple(array)))

    """测试选择排序"""
    print("""测试选择排序""")
    array = [1, 3, 5, 2, 2, 2, 10, 3, 2, 7, 19]
    print(Stack.selectSort(array))
    print(Stack.selectSort(tuple(array)))