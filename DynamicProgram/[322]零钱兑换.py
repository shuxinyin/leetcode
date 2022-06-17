# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。 
# 
#  计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 2³¹ - 1 
#  0 <= amount <= 10⁴ 
#  
#  Related Topics 广度优先搜索 数组 动态规划 👍 1972 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        '''与完全背包类似，完全背包求最大价值，这里求最少物品个数
        二维数组表示：
        状态： dp[i][j]前i种硬币达到金额j的最小硬币数
        转移： dp[i][j] = min(dp[i][j], dp[i][j-coin_i] + 1)

        一维数组表示：
        状态： dp[i]达到金额i的最小硬币数
        转移： dp[i]= min(dp[i], dp[i-coin_i] + 1)
        初始状态：dp[0] = 0， 求最小，其他的值初始化inf
        '''

        N = len(coins)
        # 类似完全背包问题
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, N + 1):
            w = coins[i - 1]
            # 正序遍历，前一个状态表示已经加了i物品，当前是第i个物品不加与加两种状态
            for j in range(w, amount + 1):
                dp[j] = min(dp[j], dp[j - w]+1)
        return dp[-1] if dp[-1] != float("inf") else -1

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    S = Solution()
    print(S.coinChange(coins, amount))