## 队列、栈

剑指 Offer 59 - I. 滑动窗口的最大值
剑指 Offer 59 - II. 队列的最大值

剑指 Offer 09. 用两个栈实现队列
剑指 Offer 30. 包含min函数的栈

剑指 Offer 29. 顺时针打印矩阵
剑指 Offer 31. 栈的压入、弹出序列

### 队列， 双边队列

#### 剑指 Offer 59 - I. 滑动窗口的最大值

Q: 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

> 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
> 输出: [3,3,5,5,6,7]
> 滑动窗口的位置 最大值
> ---------------               -----
> [1  3 -1] -3 5 3 6 7 3
> 1 [3 -1 -3] 5 3 6 7 3
> 1 3 [-1 -3  5] 3 6 7 5
> 1 3 -1 [-3  5  3] 6 7 5
> 1 3 -1 -3 [5  3  6] 7 6
> 1 3 -1 -3 5 [3  6  7]      7

```python

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ''' 双边队列
            维持一个长度为k的窗口deque，原则，保持头部head元素最大
                1. 下一个元素比tail大， 则一直pop，后append
                2. 同时 判断head是否已经出窗口了
        '''
        from collections import deque
        if not nums or k == 0:
            return []

        n = len(nums)
        window = deque()
        res = []

        # 窗口未形成
        for i in range(n):
            while window and nums[i] > window[-1]:
                window.pop()
            window.append(nums[i])
        res.append(window[0])

        # 窗口已结形成
        for i in range(n):
            # 判断当前队列最大值head 是否已经出窗口了
            if window[0] == nums[i - k]:
                window.popleft()

            while window and nums[i] > window[-1]:
                window.pop()
            window.append(nums[i])
            res.append(window[0])
        return res
```

#### 剑指 Offer 59 - II. 队列的最大值

Q: 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都
是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1


> 输入:
> ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
> [[],[1],[2],[],[],[]]
> 输出:[null,null,null,2,1,2]

```python
import queue


class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()  # 保持head最大值 双边队列
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans

```

#### 剑指 Offer 09. 用两个栈实现队列
Q: 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的
    功能。(若队列中没有元素，deleteHead 操作返回 -1 ) 

> ["CQueue","appendTail","deleteHead","deleteHead"]
> [[],[3],[],[]]
> 输出：[null,null,3,-1]

```python
class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()

        if not self.stack_in:
            return -1

        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()
```

#### 剑指 Offer 30. 包含min函数的栈
Q: 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。 

> MinStack minStack = new MinStack();
> minStack.push(-2);
> minStack.push(0);
> minStack.push(-3);
> minStack.min();   --> 返回 -3.
> minStack.pop();
> minStack.top();      --> 返回 0.
> minStack.min();   --> 返回 -2.

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

        # 小于栈顶的元素 进栈B
        if not self.stack2 or self.stack2[-1] >= x:
            self.stack2.append(x)

    def pop(self) -> None:
        if self.stack2[-1] == self.stack1.pop():
            self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def min(self) -> int:
        return self.stack2[-1]
```

#### 剑指 Offer 29. 顺时针打印矩阵
>  输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
>  示例 1： 
>  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
>  输出：[1,2,3,6,9,8,7,4,5]

```python
class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        ''' 从左向右、从上向下、从右向左、从下向上
        设置4个边界，left, right, top, bottom
        '''
        if not matrix:
            return []

        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])  # left to right
            t += 1
            if t > b:
                break
                
            for i in range(t, b + 1):
                res.append(matrix[i][r])  # top to bottom
            r -= 1
            if l > r:
                break
                
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])  # right to left
            b -= 1
            if t > b:
                break
                
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])  # bottom to top
            l += 1
            if l > r:
                break
        return res
```


#### 剑指 Offer 31. 栈的压入、弹出序列
Q: 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
    例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。 

>  输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
> 输出：true
> 解释：我们可以按以下顺序执行：
> push(1), push(2), push(3), push(4), pop() -> 4,
> push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:  # 判断出栈
                stack.pop()
                i += 1
        return not stack
```

