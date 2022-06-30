# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直
# 到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？ 
# 
#  
# 
#  示例 1: 
# 
#  输入: 
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物 
# 
#  
# 
#  提示： 
# 
#  
#  0 < grid.length <= 200 
#  0 < grid[0].length <= 200 
#  
#  Related Topics 数组 动态规划 矩阵 👍 301 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        '''
        # Time: O(MN), Space: O(MN)
        状态定义：创建比grid矩阵大一维的矩阵，列表dp[row+1][col+1]， dp[i][j]表示当前位置的最大值
        转移方程：dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])+ grid[i - 1][j - 1]
        初始状态： dp[0]=nums[0], 以nums[0]为结尾的子数组的最大连续子数组最大和nums[0]
        返回值： 返回dp[row][col]，代表最大值
        '''
        row, col = len(grid), len(grid[0])
        dp = [[0 for _ in range(col + 1)] for j in range(row + 1)]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

        return dp[row][col]

# leetcode submit region end(Prohibit modification and deletion)
