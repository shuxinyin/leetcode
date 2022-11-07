### dp之杨辉三角

杨辉三角 与 118. 杨辉三角II 是一个解题思路， 一个是生成整个杨辉三角矩阵， 另一个是生成杨辉三角第n行

### 118. 杨辉三角

Q: 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行

```python
class Solution:
    def generate(self, numRows: int) -> [[int]]:
        '''
        规律： 1 ... 1  #  头与尾都是1，中间的数=上一行 res[j-1] + res[j]
        '''
        res = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(row)
        return res
```

### 119. 杨辉三角II

Q: 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

```python
class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        '''
        状态： dp[i] 表示
        '''
        pre = []
        for i in range(rowIndex + 1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(pre[j - 1] + pre[j])
            pre = row
        return pre
```

### 931. 下降路径最小和

Q:给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和, 方向可以是走左下，右下，直下。

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        状态： dp[i][j]，走到第i行第j个数时的最小和
        转移： dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] dp[i-1][j+1]) + matrix[i][j]
        初始化：dp[i][j] = 0
        返回： dp[0][0]
        '''
        m, n = len(matrix), len(matrix[0])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
        return dp[-1][-1]
```

### 120.三角形最小路径和.py

Q: 给定一个三角形 triangle ，找出自顶向下的最小路径和。

```python

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ''' 由于自底向上与自顶向低，结果一样，自底向上只有唯一出口，返回dp[0][0]即可
        状态： dp[i][j]，走到第i行第j个数时的最小和
        转移： dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]  # 根据杨辉三角特征，必定是由（i+1, j+1）或（i+1, j） 走到（i,j）.
        初始化：dp[i][j] = 0
        返回： dp[0][0]
        '''
        n = len(triangle)

        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(0, i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]

    # leetcode submit region end(Prohibit modification and deletion)

    def minimumTotal_optimize(self, triangle: List[List[int]]) -> int:
        # 优化空间 O(n)
        n = len(triangle)

        dp = [0 for i in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(0, i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]
```