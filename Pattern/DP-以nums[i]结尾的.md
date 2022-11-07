### Question Set
53-最大子数组和  

376-摆动序列

300-最长递增子序列

918-环形子数组的最大和



#### 53-最大子数组和  
Q: 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
   子数组 是数组中的一个连续部分。 

> 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
> 输出：6
> 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

```python
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        ''' 
        状态： dp[i]表示以nums[i]结尾的最大连续子数组和
        转移： dp[i] = max(dp[i], dp[i-1] + nums[i])
        初始化： dp[0] = nums[0]
        '''
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * (n)
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i], dp[i-1] + nums[i])
        return max(dp)

```

#### 300-最长递增子序列 
Q: 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。 
  子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。 

```python
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        '''DP
        状态：dp[i] 表示以nums[i]结尾的最长增长子序列最大长度
        转移： if nums[i] > nums[j]:
                dp[i] = dp[j] +1
              else nums[i] <= nums[j]:
                continue
        综合起来： dp[i] = max(dp[i], dp[j] +1)  for j in [0, i)
        初始化： dp[i] 所有元素置 1，含义是每个元素都至少可以单独成为子序列，此时长度都为1
        返回值: max(dp)
        Time: O(N^2)
        Space: O(N)
        '''
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```


#### 376-摆动序列 
Q:  子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。 
    给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。 

> 例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。   
> 相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。 
 
> 输入：nums = [1,7,4,9,2,5]
> 输出：6
> 解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
        状态：up[i]表示以i结尾的最长向上摆动序列,down[i]表示以i结尾的最长向下摆动序列
         转移：  if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j]+1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j]+1)
        初始化： up = [1] * len(nums)
                down = [1] * len(nums)
        返回： max(max(up), max(down))
        '''

        if not nums:
            return 0

        n = len(nums)
        up = [1 for _ in range(n)]
        down = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j]+1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j]+1)
        return max(max(up), max(down))
```



#### 918-环形子数组的最大和  
Q:  给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。 
    环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。 
    子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j]，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。 

> 输入：nums = [5,-3,5]
> 输出：10
> 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10

> 输入：nums = [1,-2,3,-2]
> 输出：3
> 解释：从子数组 [3] 得到最大和 3

```python
class Solution:
    def maxSubarraySumCircular(self, nums: [int]) -> int:
        '''
        分两种情况：1. 最大子数组不跨越头尾， 正常求最大子数组和
                    2. 最大子数组跨越头尾，则反求 最小和， 最大和=sum(数组)-最小和
        综合起来：最大的环形子数组和 = max(最大子数组和，数组总和-最小子数组和)

        状态： dp[i]表示以nums[i]结尾的最大子数组和
        转移： dp[i] = max(dp[i], dp[i-1] + nums[j])
        初始化： dp[0] = nums[0] 
        '''
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, n):
            # 最大的连续子集和
            dp_max[i] = max(nums[i], dp_max[i - 1] + nums[i])

            # 最小的连续子集和
            dp_min[i] = min(nums[i], dp_min[i - 1] + nums[i])

        max_sum = max(dp_max)
        min_sum = min(dp_min)
        return max(max_sum, sum(nums) - min_sum) if max_sum > 0 else max_sum

    def maxSubarraySumCircular2(self, nums: [int]) -> int:
        # 由于状态转移方程中，dp[i]只和 dp[i - 1] 有关，可以使用滚动变量方式进行优化
        total, n = 0, len(nums)
        maxSum, curMax = nums[0], 0
        minSum, curMin = nums[0], 0

        for i in range(n):
            # 最大的连续子集和
            curMax = max(nums[i], curMax + nums[i])
            maxSum = max(maxSum, curMax)

            # 最小的连续子集和
            curMin = min(nums[i], curMin + nums[i])
            minSum = min(minSum, curMin)

            total += nums[i]
        # 如果全是负数，那么maxSum就会是负数，总和total就会等于最小和minSum, 返回值就会是0，实际应该直接返回maxSum
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
```