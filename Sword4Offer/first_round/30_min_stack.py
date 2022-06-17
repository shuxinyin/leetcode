class MinStack:
    """
    method: push: O(1), pop, min: O(1)
    使用一个入栈用来接收数据，使用一个出栈用来返回最小值。
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if not self.stack2 or self.stack2[-1] >= x:
            self.stack2.append(x)

    def pop(self) -> None:
        # two stack pop out at the same time
        if self.stack1.pop() == self.stack2[-1]:
            self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def min(self) -> int:
        return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()


class MinStackTest:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if not self.stack2 or self.stack2[-1] >= x:
            self.stack2.append(x)

    def pop(self) -> None:
        if self.stack1.pop() == self.stack2[-1]:
            self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def min(self) -> int:
        return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.min())
    print(minStack.pop())
    print(minStack.top())

    print(minStack.min())
