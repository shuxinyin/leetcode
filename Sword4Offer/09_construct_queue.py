class CQueue:
    # solution for leetcode
    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def appendTail(self, value):
        self.in_stack.append(value)

    def deleteHead(self):
        if self.out_stack:
            return self.out_stack.pop()

        if not self.in_stack:
            return -1

        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


class MyQueue1:
    """
    method1: push: O(1), pop/peek: O(n)
    使用一个入栈用来接收数据，使用一个出栈用来返回数据。
    """

    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def move(self) -> None:
        if self.out_stack == []:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self.move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return self.in_stack == self.out_stack == []


class MyQueue2:
    """
    method2: push: O(n), pop/peek: O(1)
    """

    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x: int) -> None:
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
        self.out_stack.append(x)
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        return self.out_stack.pop()

    def peek(self) -> int:
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.out_stack


class CQueueTest:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, value: int) -> None:
        self.in_stack.append(value)

    def deleteHead(self) -> int:
        while self.out_stack:
            return self.out_stack.pop()

        if not self.in_stack:
            return -1

        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()


if __name__ == '__main__':
    q1 = MyQueue1()
    print(q1.push(1))
    print(q1.push(2))
    print(q1.peek())
    # 1
    print(q1.pop())
    # 1
    print(q1.empty())
    # False

    # test q2
    q2 = MyQueue2()
    print(q2.push(1))
    print(q2.push(3))
    print(q2.peek())  # 1
    print(q2.pop())  # 1
    print(q2.peek())  # 3
    print(q2.empty())  # False
    print(q2.pop())
