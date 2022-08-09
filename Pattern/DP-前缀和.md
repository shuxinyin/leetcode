## DP-前缀和问题

### 问题合集：

64-最小路径和  
221-最大正方形  
1314-矩阵区域和  
304-二维区域和检索-矩阵不可变
1292- 
### 64-最小路径和

Q: 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 说明：每次只能向下或者向右移动一步。
> 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
> 输出：7
> 解释：因为路径 1→3→1→1→1 的总和最小。

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''DP
        状态：dp[i][j]表示到达位置（i, j）的总和。
        转移： 
            if i == j == 0:  # 初始位置[i][j]
                dp[i][j] = grid[i][j]
            elif i==0:  # 第一行dp[i][j]
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            elif j==0:  # 第一列dp[i][0]
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        初始化： dp = [[0 for _ in range(n)] for _ in range(m)]
        返回： dp[-1][-1]
        '''
        m, n = len(grid), len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == j == 0:  # 位置[i][j]
                    dp[i][j] = grid[i][j]
                elif i == 0:  # 第一行dp[i][j]
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:  # 第一列dp[i][0]
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
```

### 221-最大正方形

Q: 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
> 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"], ["1","0","0","1","0"]]
> 输出：4

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''DP
        状态： dp[i][j]是表示以位置（i, j）为右下角的正方形边长。
        转移：   取正方形的四个顶点，进行判断，取min
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        初始化： dp[i][0] = maxtrix[i][0], dp[0][j] = maxtrix[0][j] 
        '''

        m, n = len(matrix), len(matrix[0])

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        dp = [[0 for i in range(n)] for j in range(m)]
        # 第一行        
        for i in range(m):
            dp[i][0] = matrix[i][0]
        # 第一列
        for j in range(m):
            dp[0][j] = matrix[0][j]

        maxSide = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            maxSide = max(maxSide, dp[i][j])

        return maxSide * maxSide  
```

### 1314-矩阵区域和

Q: 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和：
1.i - k <= r <= i + k, 2. j - k <= c <= j + k 且 (r, c) 在矩阵内。

> 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
> 输出：[[12,21,16],[27,45,33],[24,39,28]]

```python
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        '''DP
        状态：dp[i][j] 表示矩形对角点（i, j）到（0， 0）区域和
        转移： 
             dp[x][y] = dp[x][y - 1] + dp[x - 1][y] - dp[x - 1][y - 1] + mat[x - 1][y - 1]
        初始化：[[0 for _ in range(n + 1)] for _ in range(m + 1)]
        '''

        # Time: O(m * n * min(m, n))
        # Space: O(m * n)
        m, n = len(mat), len(mat[0])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # 区域内矩阵和
        for x in range(1, m + 1):
            for y in range(1, n + 1):
                dp[x][y] = dp[x][y - 1] + dp[x - 1][y] - dp[x - 1][y - 1] + mat[x - 1][y - 1]

        def get(x, y):
            # 保证坐标(x,y)不出界
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return dp[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 前缀和
                # 由于dp shape = [m+1, n+1], 故(i, j)真实表示位置为dp(i+1, j+1)
                ans[i][j] = get(i + 1 + k, j + 1 + k) - get(i - k, j + 1 + k) -
                            get(i + 1 + k, j - k) + get(i - k, j - k)
        return ans

```

### 303-区域和检索-数组不可变

Q: (一维) # 给定一个整数数组 nums，处理以下类型的多个查询: 计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right.
> 输入： ["NumArray", "sumRange", "sumRange", "sumRange"]  
> [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]  
> 输出： [null, 1, -1, -3]
> presum = [0, -2, -2, 1, -4, -2, -3]

```python
class NumArray:
    '''
        nums = [1, 2, 3, 4], self.sums=[0, 1, 3, 6, 10], pre_sum[1, 2] = 
        nums 数组的每一项都对应有它的前缀和dp： nums 的第 0 项到 当前项 的和。
        用数组 preSum 表示，preSum[i]：第 0 项到 第 i 项 的和。
            preSum[i]=nums[0]+nums[1]+…+nums[i]
        易得，nums 的某项 = 两个相邻前缀和的差：
            nums[i]=preSum[i]−preSum[i−1]
        对于 nums 的 i 到 j 的元素和，上式叠加，有：
            nums[i]+…+nums[j]=preSum[j]−preSum[i−1]
    '''

    def __init__(self, nums: List[int]):
        self.presums = [0]

        for num in nums:
            self.presums.append(self.presums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.presums[j + 1] - self.presums[i]


```

### 304-二维区域和检索-矩阵不可变

Q: (二维) 给定一个二维矩阵 matrix，以下类型的多个请求： 计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        '''DP  求区域内矩阵和
        状态：dp[i][j] 表示矩形对角点（i, j）到（0， 0）区域和
        转移： 
             dp[x][y] = dp[x][y - 1] + dp[x - 1][y] - dp[x - 1][y - 1] + mat[x - 1][y - 1]
        初始化：[[0 for _ in range(n + 1)] for _ in range(m + 1)]
        '''
        if not matrix or not matrix[0]:
            M, N = 0, 0
        else:
            M, N = len(matrix), len(matrix[0])

        self.dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                self.dp[i][j] = self.dp[i][j - 1] + self.dp[i - 1][j] - self.dp[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    
        presum = self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + \
                 self.dp[row1][col1]   
        return presum

```

### 
# 前缀问题  1292  https://www.bilibili.com/video/BV19J41147jQ?spm_id_from=333.337.search-card.all.click
```python
class Solution:
    def matrixBlockSum(self, mat: [[int]], threshold: int) -> [[int]]:
        # Time: O(m * n * min(m, n))
        # Space: O(m * n)
        m, n = len(mat), len(mat[0])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for y in range(1, m + 1):
            for x in range(1, n + 1):
                dp[y][x] = dp[y][x - 1] + dp[y - 1][x] - dp[y - 1][x - 1] + mat[y - 1][x - 1]

        def rangeSum(x1, y1, x2, y2):
            return dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 - 1][x1 - 1]

        ans = 0
        for y in range(1, m + 1):
            for x in range(1, n + 1):
                k = 0
                while y + k <= m and x + k <= n:
                    res = rangeSum(x, y, x + k, y + k)
                    if res > threshold:
                        break
                    ans = max(ans, k + 1)
                    k += 1

        return ans
```