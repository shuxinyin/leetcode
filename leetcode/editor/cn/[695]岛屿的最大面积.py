# 给你一个大小为 m x n 的二进制矩阵 grid 。 
# 
#  岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都
# 被 0（代表水）包围着。 
# 
#  岛屿的面积是岛上值为 1 的单元格的数目。 
# 
#  计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
# [0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 50 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 702 👎 0

# why 这题不需要将土地重新置1， 79需要重新置1
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maxAreaOfIsland(self, grid):
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                ans = max(self.dfs(i, j, grid), ans)
        return ans

    def dfs(self, i, j, grid):
        if i < 0 or j < 0 \
                or i == len(grid) or j == len(grid[0]) \
                or grid[i][j] != 1:
            return 0

        grid[i][j] = 0  # 表示此地已用
        ans = 1
        for direc in self.directs:
            cur_i = i + direc[0]
            cur_j = j + direc[1]

            ans += self.dfs(cur_i, cur_j, grid)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
