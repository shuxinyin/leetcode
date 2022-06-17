# 泰波那契序列 Tn 定义如下： 
# 
#  T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2 
# 
#  给你整数 n，请返回第 n 个泰波那契数 Tn 的值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#  
# 
#  示例 2： 
# 
#  输入：n = 25
# 输出：1389537
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 37 
#  答案保证是一个 32 位整数，即 answer <= 2^31 - 1。 
#  
#  Related Topics 记忆化搜索 数学 动态规划 👍 205 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tribonacci(self, n: int) -> int:
        ''' DP
        状态： dp[i]表示第i项的值
        转移： dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        初始状态： dp[0]=0, dp[1]=1, dp[2]=1
        与fibo一样，把0，1，2三种情况概括进来的写法
        n=0, (0, 1, 1)
        n=1, (1, 1, 2)
        n=2, (1, 2, 4)
        n=3, (2, 4, 7)
        ... a的值表示当前位置的值
        '''
        a, b, c = 0, 1, 1
        for i in range(n):
            tmp1, tmp2 = a, b
            a = b
            b = c
            c += tmp1 + tmp2
        return c

# leetcode submit region end(Prohibit modification and deletion)
