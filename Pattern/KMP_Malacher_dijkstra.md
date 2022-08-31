## 经典算法

### KMP

28-实现 strStr()


#### KMP算法
主要是要计算前缀部分匹配表(Partial Match Table)的数组， 也称为next数组；  
表示在s[i：j]子串中，前缀与后缀完全匹配的最大长度
![PMT](img.png)

#### 题目
##### 28-实现 strStr()

> 实现 strStr() 函数。
> 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如
> 果不存在，则返回 -1 。
> 说明：
> 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
> 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

> 示例 1：
> 输入：haystack = "hello", needle = "ll"
> 输出：2

```python
class Solution:
    def strStr(self, text: str, pattern: str) -> int:
        '''
        next： 为前缀表，采用的是前后缀最长相等位置长度 - 1
        j: text后缀组末尾, 逐个匹配
        p: pattern末尾
        1. 初始化 2.前后缀不相同 3.前后缀相同  4.get_next
        '''
        len_pattern = len(pattern)
        len_text = len(text)
        if len_pattern == 0:
            return 0
        next = self.getnext(pattern)
        print(next)
        p = -1
        for j in range(len_text):
            while p >= 0 and pattern[p + 1] != text[j]:
                p = next[p]
            if pattern[p + 1] == text[j]:
                p += 1
            if p == len_pattern - 1:
                return j - len_pattern + 1
        return -1

    def getnext(self, pattern):
        '''
        next： 为前缀表，采用的是前后缀最长相等位置长度 - 1
        j: 前缀组末尾
        i: 后缀组末尾
        1. 初始化 2.前后缀不相同 3.前后缀相同  4.get_next
        '''
        next = ['' for i in range(len(pattern))]
        j = -1  # 就是看冲突位置的下标即可
        next[0] = j
        for i in range(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]:
                # 不匹配，回退到冲突位置的下标指示位置，继续匹配
                j = next[j]
            if pattern[j + 1] == pattern[i]:
                j += 1
            next[i] = j
        return next
```