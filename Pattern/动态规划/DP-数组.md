### Question Set

#### 152--乘积最大数组
Q: 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 

> 输入: nums = [2,3,-2,4]
> 输出: 6
> 解释: 子数组 [2,3] 有最大乘积 6。

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ''' 
        状态：dp[i] 表示 以nums[i]结尾的最大连续子数组乘积
        转移：dp[i] = max(dp[i], dp[i-1] * nums[i])
        初始状态：dp[0] = nums[0]

        '''
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)
        dp = [0] * len(nums)
        max_dp[0], min_dp[0] = nums[0], nums[0]

        dp[0] = nums[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            dp[i] = max(max_dp[i], dp[i-1])
        return dp[-1]
    
    def maxProduct(self, nums: [int]) -> int:
        ''' 求最大乘积，因为负数 * 负数 = 正数，负数乘积imin可能变imax， imax, imin
            转移： imax = max(imax*nums[i], nums[i])  # 保证imax是最大值
                  imin = min(imin*nums[i], nums[i])
                  max_val = max(imax, imin)
        '''

        n = len(nums)
        max_value = float("-inf")
        imax, imin = 1, 1
        for i in range(n):
            if nums[i] < 0:
                imax, imin = imin, imax

            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])

            max_value = max(max_value, imax)

        return max_value  

```


#### 1567-乘积为正数的最长子数组长度

Q: 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。 一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。  
    请你返回乘积为正数的最长子数组长度。 

> 输入：nums = [1,-2,-3,4]
> 输出：4
> 解释：数组本身乘积就是正数，值为 24 。

```python
class Solution:
    def getMaxLen(self, nums: [int]) -> int:
        '''
        状态： pos[i]表示下标i结尾的乘积为正数的最长子数组长度
             neg[i]表示下标i结尾乘积为负数的最长子数组长度。

        转移：i>1时：
                ①. nums[i]>0, 之前的乘积*nums[i]不改变乘积正负性
                    pos[i] = pos[i-1]+1
                    neg[i] = neg[i-1] + 1, if neg[i-1]>0
                    neg[i] = 0, if neg[i-1]=0
                ②. nums[i]<0, 之前的乘积*nums[i]改变乘积正负性
                    pos[i] = neg[i-1]+1, if neg[i-1]>0
                    pos[i] = 0, if neg[i-1]=0
                    neg[i] = pos[i-1] + 1
                ③.当 nums[i]=0时，
                    以下标i结尾的子数组的元素乘积一定为0，因此有 positive[i]=0, negative[i]=0。

        初始状态：i=0: if nums[0] > 0, positive[0] = 1
                    if nums[0] < 0, negative[0] = 1
        '''
    
        length = len(nums)
        positive, negative = [0] * length, [0] * length
        if nums[0] > 0:
            positive[0] = 1
        elif nums[0] < 0:
            negative[0] = 1

        maxLength = positive[0]
        for i in range(1, length):
            if nums[i] > 0:
                positive[i] = positive[i - 1] + 1
                negative[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
            elif nums[i] < 0:
                positive[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
                negative[i] = positive[i - 1] + 1  # 
            else:
                positive[i] = negative[i] = 0
            maxLength = max(maxLength, positive[i])

        return maxLength
    
    def getMaxLen2(self, nums: [int]) -> int:
        ''' 滚动数组
        '''
        n = len(nums)
        pos = 1 if nums[0] > 0 else 0
        neg = 1 if nums[0] < 0 else 0

        max_len = pos

        for i in range(1, n):
            if nums[i] > 0:
                pos += 1
                neg = (neg + 1 if neg > 0 else 0)

            elif nums[i] < 0:
                new_pos = (neg + 1 if neg > 0 else 0)
                new_neg = pos + 1
                pos, neg = new_pos, new_neg

            else:
                pos = neg = 0
            max_len = max(max_len, pos)
        return max_len
```


#### 413-等差数列划分
Q: 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。 
    例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。 

> 输入：nums = [1,2,3,4]
> 输出：3
> 解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。

```python
class Solution:
    def numberOfArithmeticSlices(self, nums: [int]) -> int:
        '''
        状态： dp[i] 表示 以 nums[i] 结尾的子序列的等差数据列个数
        转移： dp[i] = dp[i-1] + 1
        初始状态： dp[0]=dp[1]=0
        返回： sum(dp)
        dp = [0] * n
        for i in range(2, n):
            dp[i] = dp[i - 1] + 1 if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2] else 0
        return sum(dp)
        '''
        n = len(nums)
        if n < 3:
            return 0

        dp = [0] * n
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] +1
            else:
                dp[i] = 0
        return sum(dp)
```



#### 91-解码方法

Q: 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：  'A' -> "1", 'B' -> "2" ... 'Z' -> "26" 
    要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为： 
      "AAJF" ，将消息分组为 (1 1 10 6) , "KJF" ，将消息分组为 (11 10 6) 
    注意，消息不能分组为 (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。 
    给你一个只含数字的 非空 字符串 s ，请计算并返回 解码方法的 总数 。 题目数据保证答案肯定是一个 32 位 的整数。 


> 输入：s = "226"
> 输出：3
> 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。


```python
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        状态：dp[i]表示以s[i]结尾的 解码方法 的总数
        转移： 分为两种情况： 当前字符为 0 否？
            if s[i] == 0:
                # 10 or 20 必须绑定在一起翻译， dp[i] = dp[i - 2]
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] = dp[i - 2]
                else
                    return 0
            else
                if 10<s[i-1:i+1] <27:  # 可分开逐个或 在一起翻译
                    dp[i] = dp[i-2] + dp[i-1]
                else:
                    dp[i] = dp[i-1]  # 必须分开，逐个翻译
        初始状态：  dp[0] = dp[-1] = 1, (为了把dp)
        # 由于 dp[i-2]的存在，所以 dp 的长度要 len（s）+1 ，留出 dp[-1] = 1
        返回： dp[n-1]
        '''

        n = len(s)
        dp = [1] * (n + 1)
        dp[0] = dp[-1] = 1

        for i in range(1, n):
            if s[i] == '0':
                # 10 or 20 必须绑定在一起翻译， dp[i] = dp[i - 2]
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                if '10' < s[i - 1:i+1] < '27':  # 可分开逐个或 在一起翻译
                    dp[i] = dp[i - 2] + dp[i - 1]
                else:
                    dp[i] = dp[i - 1]  # 必须分开，逐个翻译
        return dp[n-1]
```

