##  DP-字符串问题

### 问题合集：

5-最长回文子串  
516-最长回文子序列  
300-最长递增子序列  
376-摆动序列
392-判断子序列  
1143-最长公共子序列  
72-编辑距离


### 5-最长回文子串
Q: 给你一个字符串 s，找到 s 中最长的回文子串。
> 输入：s = "babad" 输出："bab"  
> 解释："aba" 同样是符合题意的答案。

```python
class Solution:
    def expandAroundCenter(self, s, left, right):
        ''' 中心字符扩展判断
        left, right 分别为回文字符串的左、右边界
        '''
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        ''' 中心扩展算法：枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止
            回文子串存在两种情况： 1. cbabc(奇数), 2. cbbc（偶数）
            Time: O(n^2)
            Space: O(1)
        '''
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)  # 1. cbabc(奇数)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)  # 2. cbbc（偶数）

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]
        
```


### 516-最长回文子序列  
Q: 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。 
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。 

> 输入：s = "bbbab" 输出：4  
> 解释：一个可能的最长回文子序列为 "bbbb" 。

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''DP
        状态： dp[i][j]表示s[i:j+1]中最长回文序列长度
        转移： if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
              else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            注意： i 倒序遍历,  j从i+1往后遍历， 保证子问题dp[i+1][j], dp[i][j-1]已经算好
        初始化： dp[i][i] = 1, 单个字符最长回文序列是1
        '''

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]


```


### 300-最长递增子序列 
Q: 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。 
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。 
 
> 输入：nums = [10,9,2,5,3,7,101,18]
> 输出：4  
> 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

```python
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        '''DP
        状态：dp[i] 表示以nums[i]结尾的最长增长子序列最大长度(是以nums[i]结尾)
        转移：if nums[i] > nums[j]:
                dp[i] = dp[j] + 1
             else:
                 continue
        综合： dp[i] = max(dp[i], dp[j] + 1) if nums[j] < nums[i]
        初始化：dp = [1 for _ in range(n)]
        返回： max(dp)
        '''
        n = len(nums)
        dp = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    
    def lengthOfLIS_DoubleDevided(self, nums: [int]) -> int:
        '''
        状态：tails[i] 表示长度为i+1的子序列尾部元素的值
        如 [1,4,6]序列，长度为 1,2,3的子序列尾部元素值分别为 tails=[1,4,6]
        转移：
        1. 区间中存在 tails[i]>nums[k]： 将第一个满足 tails[i]>nums[k] 执行 tails[i]=nums[k]；因为更小的 nums[k] 后更可能接一个比它大的数字。
        2. 区间中不存在 tails[i]>nums[k]： 意味着 nums[k] 可以接在前面所有长度的子序列之后，因此肯定是接到最长的后面（长度为 res），新子序列长度为 res+1。

        综合起来：
        初始化： dp[i] 所有元素置 1，含义是每个元素都至少可以单独成为子序列，此时长度都为1
        返回值:
        Time: O(NlogN)
        Space: O(N)
        '''
        # Dynamic programming + Dichotomy.
        pass
```

### 376-摆动序列
Q: 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。
第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。 

> 输入：nums = [1,7,4,9,2,5]  输出：6
  解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。
```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''DP-与300类似
        状态：up[i]表示以nums[i]结尾的最长向上摆动序列,down[i]表示以nums[i]结尾的最长向下摆动序列
        转移：if nums[i] > nums[j]:
                up[i] = max(up[i], down[j]+1)
            elif nums[i] < nums[j]:
                down[i] = max(down[i], up[j]+1)
        初始状态：up = [1 for _ in range(n)]
                 down = [1 for _ in range(n)]
        '''
        up = [1 for _ in range(n)]
        down = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j]+1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j]+1)
        return max(max(up), max(down))
```



### 392-判断子序列  
Q: 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。 
> 输入：s = "abc", t = "ahbgdc"  
> 输出：true  

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''SinglePointer
        '''
        if not s:
            return True

        p = 0
        for t0 in t:
            if s[p] == t0:
                p += 1

        if p == len(s):
            return True
        return False
```
1143-最长公共子序列 
Q: 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
> 输入：text1 = "abcde", text2 = "ace"   
> 输出：3    
> 解释：最长公共子序列是 "ace" ，它的长度为 3 。  

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''DP
        状态： dp[i][j] 表示s1[:i]与s2[:j]的公共字符序列长度
        转移： if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
              else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        初始化： dp = [[0 for i in range(n+1)] for j in range(m+1)] 
                dp[0][j] 表示s1[:0]与s2[:j]的公共字符序列长度为0
                dp[i][0] 表示s1[:i]与s2[:0]的公共字符序列长度为0
        返回： dp[-1][-1]
        '''
        m, n = len(text1), len(text2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
```

72-编辑距离
Q: 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。 
  你可以对一个单词进行如下三种操作： 1.插入一个字符   2.删除一个字符   3.替换一个字符 

>  输入：word1 = "horse", word2 = "ros"  输出：3
> 解释：
> horse -> rorse (将 'h' 替换为 'r')
> rorse -> rose (删除 'r')
> rose -> ros (删除 'e')

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''DP
        状态： dp[i][j] 表示s1[:i]与s2[:j]所使用的最少操作数
        转移： if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
              else:
                # dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        初始化： dp = [[1 for i in range(n+1)] for j in range(m+1)] 
                dp[0][j]=dp[0][j-1] + 1 表示s1[:0]到s2[:j]需使用的操作数
                dp[i][0]=dp[i-1][0] + 1 表示s1[:i]到s2[:0]需使用的操作数
        返回： dp[-1][-1]
        '''
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        # 第一行，是s1为空变成s2最少步数，就是插入操作
        for i in range(1, n2 + 1):
            dp[0][i] = dp[0][i - 1] + 1

        # 第一列，是s2为空变成s1最少步数，就是删除操作
        for i in range(1, n2 + 1):
            dp[i][0] = dp[i-1][0] + 1

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]
```