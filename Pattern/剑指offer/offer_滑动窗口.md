## 滑动窗口

面试题17.18 最短超串
剑指offer59-I.的最大值
剑指offer59-II.队列的最大值


### 面试题17.18 最短超串
> 假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。 
>  返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。 

>  示例 1: 
>  输入:
>  big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
>  small = [1,5,9]
>  输出: [7,10] 


```python
class Solution:
    def shortestSeq(self, big, small):
        import collections
        minl, minr = -1, -1
        l, r = 0, 0
        min_len = len(big)
        need = collections.Counter(small)
        diff = len(small)

        while r < len(big):
            if big[r] in need:
                need[big[r]] -= 1
                if need[big[r]] >= 0:
                    diff -= 1
            
            # 在此窗口内 找最小， 同时移动左边
            while diff == 0:
                if r - l < min_len:
                    min_len = r - l
                    minl, minr = l, r

                if big[l] in need:  # 移动左边
                    need[big[l]] += 1
                    if need[big[l]] > 0:
                        diff += 1
                l += 1
            r += 1

        if minl == -1:
            return []
        return [minl, minr]
```


### 剑指 Offer 59 - I 滑动窗口的最大值
> 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。 

> 示例: 
> 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
> 输出: [3,3,5,5,6,7] 
> 解释: 
> 
>   滑动窗口的位置                最大值
> ---------------               -----
> [1  3  -1] -3  5  3  6  7       3
>  1 [3  -1  -3] 5  3  6  7       3
>  1  3 [-1  -3  5] 3  6  7       5
>  1  3  -1 [-3  5  3] 6  7       5
>  1  3  -1  -3 [5  3  6] 7       6
>  1  3  -1  -3  5 [3  6  7]      7 

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
        for i in range(k):
            while window and nums[i] > window[-1]:
                window.pop()
            window.append(nums[i])
        res.append(window[0])

        # 窗口已结形成
        for i in range(k, n):
            # 判断当前队列最大值head 是否已经出窗口了
            if window[0] == nums[i-k]:
                window.popleft()

            while window and nums[i] > window[-1]:
                window.pop()
            window.append(nums[i])
            res.append(window[0])
        return res
```


### 剑指 Offer 59 - II 队列的最大值

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
