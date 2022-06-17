class Solution:
    def maxValue(self, grid) -> int:
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


if __name__ == '__main__':
    nums = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]

    S = Solution()
    print(S.maxValue(grid=nums))