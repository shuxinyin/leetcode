# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。 
# 
#  请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。 
# 
#  假设每一种面额的硬币有无限个。 
# 
#  题目数据保证结果符合 32 位带符号整数。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：amount = 5, coins = [1, 2, 5]
# 输出：4
# 解释：有四种方式可以凑成总金额：
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#  
# 
#  示例 2： 
# 
#  
# 输入：amount = 3, coins = [2]
# 输出：0
# 解释：只用面额 2 的硬币不能凑成总金额 3 。
#  
# 
#  示例 3： 
# 
#  
# 输入：amount = 10, coins = [10] 
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 300 
#  1 <= coins[i] <= 5000 
#  coins 中的所有值 互不相同 
#  0 <= amount <= 5000 
#  
#  Related Topics 数组 动态规划 👍 863 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''与完全背包类似，完全背包求最大价值，这里求物品个数
        一维数组表示：
        状态： dp[i]达到金额i的硬币组合数
        转移： dp[i] += dp[i - coin[i]]
        初始状态：dp[0] = 1，其他的值初始化0
        '''
        N = len(coins)
        # 类似完全背包问题
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(1, N + 1):
            w = coins[i - 1]
            for j in range(w, amount + 1):
                dp[j] += dp[j - w]
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
