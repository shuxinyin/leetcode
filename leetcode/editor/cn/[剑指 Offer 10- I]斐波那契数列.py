# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下： 
# 
#  
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1. 
# 
#  斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。 
# 
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 5
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 100 
#  
#  Related Topics 记忆化搜索 数学 动态规划 👍 368 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fib(self, n: int) -> int:
        '''
        Time: O(log(N)), Space: O(1)
        f[i]: 表示斐波那契（Fibonacci）数列的第 n 项
        转移： f[i] = f[i-1] + f[i-2], i>1
        初始状态：f[0] = 0, f[1]=1
        example:
            i=0: {0, 1}
            i=1: {1, 1}
            i=2: {1, 2}
            上一状态：{a, b}, 下一状态：{b, a+b}, 此方法可把i=0, i=1, 纳入循环之中，不用单独考虑
        '''

        a, b = 0, 1
        for i in range(1, n + 1):
            tmp = a
            a = b
            b = tmp + b
        return a % 1000000007

# leetcode submit region end(Prohibit modification and deletion)
