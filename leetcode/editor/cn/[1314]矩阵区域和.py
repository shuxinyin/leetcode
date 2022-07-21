# 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 
# mat[r][c] 的和： 
# 
#  
#  i - k <= r <= i + k, 
#  j - k <= c <= j + k 且 
#  (r, c) 在矩阵内。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
#  
# 
#  示例 2： 
# 
#  
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n, k <= 100 
#  1 <= mat[i][j] <= 100 
#  
#  Related Topics 数组 矩阵 前缀和 👍 140 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
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
                ans[i][j] = get(i + 1 + k , j + 1 + k ) - get(i - k, j + 1 +  k) - \
                            get(i + 1 + k, j - k) + get(i - k, j - k)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
