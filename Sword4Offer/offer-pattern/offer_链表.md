## 滑动窗口

[剑指 Offer 06]从尾到头打印链表
[剑指 Offer 24]反转链表
[剑指 Offer 35]复杂链表的复制

[剑指 Offer 18]删除链表的节点
[剑指 Offer 22]链表中倒数第k个节点

[剑指 Offer 25]合并两个排序的链表
[剑指 Offer 52]两个链表的第一个公共节点


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
