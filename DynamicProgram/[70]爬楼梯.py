# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶 
# 
#  示例 2： 
# 
#  
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 45 
#  
#  Related Topics 记忆化搜索 数学 动态规划 👍 2461 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        ''' DP
        状态： dp[i]表示到第i阶的方法数
        转移： dp[i] = dp[i-1] + dp[i-2]， 表示当前状态可由最后爬一阶或两阶达到
        初始状态： dp[0]=0, dp[1]=1
        n=0, (0, 0, 1) 初始状态
        n=1, (0, 1, 1)
        n=2, (1, 1, 2)
        n=3, (1, 2, 3)
        ... c的值表示当前位置的值
        '''

        a, b, c = 0, 0, 1
        for i in range(1, n + 1):
            a = b
            b = c
            c = a + b
        return c

    # leetcode submit region end(Prohibit modification and deletion)
