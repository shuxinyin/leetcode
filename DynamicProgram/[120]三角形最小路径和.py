# 给定一个三角形 triangle ，找出自顶向下的最小路径和。 
# 
#  每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果
# 正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#  
# 
#  示例 2： 
# 
#  
# 输入：triangle = [[-10]]
# 输出：-10
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= triangle.length <= 200 
#  triangle[0].length == 1 
#  triangle[i].length == triangle[i - 1].length + 1 
#  -10⁴ <= triangle[i][j] <= 10⁴ 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？ 
#  
#  Related Topics 数组 动态规划 👍 1063 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
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
# leetcode submit region end(Prohibit modification and deletion)
