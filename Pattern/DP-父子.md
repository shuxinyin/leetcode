### DP-父子题

198.打家劫舍
213.打家劫舍II

55.跳跃游戏
45.跳跃游戏II

62.不同路径
63.不同路径II

42.接雨水
42.接雨水II

#### 198.打家劫舍

Q: 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。


> 输入：[1,2,3,1]
> 输出：4
> 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
> 偷窃到的最高金额 = 1 + 3 = 4 。

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            状态：dp[i]表示以nums[i]结尾的子数组最高金额
            转移：dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            初始化： dp[0]=nums[0]
        '''
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


```

#### 213.打家劫舍II

Q: 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈
，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的
房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

> 输入：nums = [2,3,2]
> 输出：3
> 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''与198类似， 切换成两种分别求，一种选尾不选头nums[1:]， 另一种选头不选尾部是nums[:-1]
        状态： dp[i]到前i家时的偷窃到的最高金额
        转移： dp[i] = max(dp[i-1], dp[i-2]+nums[i])  # 不偷i位置 或 选偷i位置
        初始状态：dp[0] = 0， dp[1] =  nums[0]
        '''

        def helper(nums: [int]) -> int:
            n = len(nums)
            dp = [0] * (n + 1)
            dp[1] = nums[0]
            for i in range(2, n + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

            return dp[-1]

        return max(helper(nums[:-1]), helper(nums[1:])) if len(nums) != 1 else nums[0]

```

#### 740-删除并获得点数

Q: 给你一个整数数组 nums ，你可以对它进行一些操作。
每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。
开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

> 输入：nums = [3,4,2]
> 输出：6
> 解释：
> 删除 4 获得 4 个点数，因此 3 也被删除。之后，删除 2 获得 2 个点数。总共获得 6 个点数。

```python
class Solution:
    def deleteAndEarn(self, nums: [int]) -> int:
        '''转化为打家劫舍问题
        nums = [2,2,3,3,3,4]  ->  count_list = [0,0,2,3,1]，index表示num=2有有两个，num=3有三个...
        这样就转化为打家劫舍问题，不能选邻居点
        状态： dp[i]表示删除第i个数时达到的最高点数
        转移： dp[i] = max(dp[i-1], dp[i-2]+count_list[i]*i)  # 不偷i位置 或 选偷i位置
        初始状态：dp[0] = 0， dp[1] =  count_list[1]
        '''
        if not nums:
            return 0

        n = max(nums)
        count_list = [0] * (n + 1)
        for num in nums:
            count_list[num] += 1

        dp = [0] * (n + 1)
        dp[1] = count_list[1]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + count_list[i] * i)
        return dp[-1]

    def deleteAndEarn2(self, nums: List[int]) -> int:
        '''降空间 O(1)
        '''
        if not nums:
            return 0

        n = max(nums)
        A = [0] * (n + 1)
        for num in nums:
            A[num] += 1

        pre, cur = 0, A[1]
        for i in range(2, n + 1):
            # cur = dp[i-1], pre = dp[i-2]
            pre, cur = cur, max(pre + A[i] * i, cur)
        return cur
```

#### 55.跳跃游戏

Q: 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。 判断你是否能够到达最后一个下标。

> 输入：nums = [2,3,1,1,4]
> 输出：true
> 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

> 输入：nums = [3, 2, 1, 0, 4]
> 输出：false
> 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ''' 
        状态： dp[i]表示能到达的最远距离：
        转移：dp[i] = max(dp[i-1], dp[i-1] + nums[i])
        初始状态：dp[0] = nums[0]
        '''
        pass

    def canJump(self, nums: List[int]) -> bool:
        ''' 一个变量： 维持一个尾标end, 表示能到的最远距离
        '''

        n = len(nums)

        end = 0  # 至今能走到的最远位置
        for i in range(n - 1):
            step = nums[i]

            if end < i:  # 当前位置i 超出了 当前能到的最远距离
                return False

            end = max(end, i + step)
        return end >= n - 1
```

#### 45.跳跃游戏II

Q: 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。 数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用 最少的跳跃次数 到达数组的最后一个位置。 假设你总是可以到达数组的最后一个位置。

> 输入: nums = [2,3,1,1,4]
> 输出: 2
> 解释: 跳到最后一个位置的最小跳跃数是 2。从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

```python

class Solution:
    def jump(self, nums: List[int]) -> int:
        ''' 两个变量：end maxPos 
            # maxPos：当前能到的最远位置
            # end：上一步时，能到的最远位置
            # step：步数
        '''
        n = len(nums)

        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])

                # 只有当前位置i到了前i步能到的最远位置，才需要step+1
                if i == end:
                    end = maxPos
                    step += 1
        return step
```

#### 62.不同路径

Q: 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

> 输入：m = 3, n = 7
> 输出：28

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ''' 
        状态： dp[i][j]表示到位置(i, j)路径数量
        转移： dp[i][j] = dp[i-1][j] + d[i][j-1]
        初始化： dp = [[1] * n for _ in range(m)] 
        '''
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
```

#### 63.不同路径II

Q: 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。


> 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
> 输出：2
> 解释：3x3 网格的正中间有一个障碍物。
> 从左上角到右下角一共有 2 条不同的路径：
> 1. 向右 -> 向右 -> 向下 -> 向下
> 2. 向下 -> 向下 -> 向右 -> 向右

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        '''
        状态： dp[i][j]表示到位置[i,j]的路径数量
        转移： if obstacleGrid[i][j] == 0: dp[i][j] = dp[i-1][j] + dp[i][j-1])
        初始化： 将第一行无障碍的置1，有障碍及障碍后续置0
                将第一列无障碍的置1，有障碍及障碍后续置0
        '''
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
```

#### 42.接雨水

Q: 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

> 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
> 输出：6
> 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

```python
class Solution:
    def trap(self, height):
        # 边界条件
        if not height: return 0
        n = len(height)

        left, right = 1, n - 2  # 分别位于输入数组的两端
        max_left, max_right = height[0], height[n - 1]
        res = 0

        while left <= right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)
            # 下面这两种情况,保证了现在在计算的位置一定是不大于左右的，保证了局部最小
            # 这样就免去了，每个位置都去搜索全局最大（如方法2）
            # 1.保证了 h[left]<=max_left<max_right
            # 2.保证了 h[right]<=max_right<max_left
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1

        return res
``` 

#### 42.接雨水II
Q: 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。 

> 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
> 输出: 4
> 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。

