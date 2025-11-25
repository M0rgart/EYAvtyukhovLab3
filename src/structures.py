class Node:
    def __init__(self, value, next_done=None):
        self.value = value
        self.next = next_done


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
        self._min = None

    def __len__(self):
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def min(self) -> int:
        if self.is_empty():
            raise IndexError('stack is empty')
        return self._min

    def _new_min(self):
        if self.is_empty():
            self._min = None
            return

        x = self.top
        self._min = x
        while x:
            if x.value < self._min:
                self._min = x.value
            x = x.next

    def push(self, x: int) -> None:
        new_node = Node(x, self.top)
        self.top = new_node
        self._size += 1
        if self._min is None or self._min > x:
            self._min = x

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('stack is empty')

        value = self.top.value
        self.top = self.top.next
        self._size -= 1

        if value == self._min:
            self._new_min()

        return value

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError('stack is empty')
        return self.top.value

class Queue:
    def __init__(self):
        self._front = None
        self.back = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def enqueue(self, x: int) -> None:
        new_node = Node(x)
        if self.back is None:
            self._front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        self._size += 1

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError('queue is empty')
        value = self._front.value
        self._front = self._front.next

        if self._front is None:
            self.back = None

        self._size -= 1
        return value

    def front(self) -> int:
        if self.is_empty():
            raise IndexError('queue is empty')
        return self._front.value