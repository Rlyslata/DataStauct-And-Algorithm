from CircularLinkedList import LinkedList, Node
from Stack import EmptyError


class Queue(LinkedList):
    def __init__(self):
        super(Queue, self).__init__()

    def enQueue(self, value):
        new_node = Node(value=value, Next=None)
        self.tail.next = new_node
        self.tail = self.tail.next

    def deQueue(self):
        if self.sentinel.next:
            value = self.sentinel.next.value
            self.sentinel.next = self.sentinel.next.next
            return value
        raise EmptyError("队列为空，不能进行出队操作")


if __name__ == "__main__":
    queue = Queue()
    queue.enQueue(1)
    queue.enQueue(2)

    print(queue.deQueue())
    print(queue.deQueue())
    try:
        print(queue.deQueue())
    except Exception as e:
        print(e.args)