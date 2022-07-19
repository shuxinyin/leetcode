# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。 
# 
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
#  例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4 
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁴ 
#  
#  Related Topics 广度优先搜索 数学 动态规划 👍 1426 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSquares(self, n: int) -> int:
        '''
        状态： dp[i] 表示数字i, 和为 i 的完全平方数的最少数量
        转移: while j*j <= i:
                dp[i] = min(dp[i], dp[i - j*j]+1)
        初始化： dp[0] = 0
        时间复杂度：O(n∗sqrt(n))
        '''
        dp = [0] * (n + 1)

        for i in range(n + 1):
            # 存在这种情况，4 =1 + 1 + 1 + 1
            dp[i] = i

            j = 0
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    S = Solution()
    print(S.numSquares(12))
