# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。 
# 
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  输入：n = 7
# 输出：21
#  
# 
#  示例 3： 
# 
#  输入：n = 0
# 输出：1 
# 
#  提示： 
# 
#  
#  0 <= n <= 100 
#  
# 
#  注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/ 
# 
#  
#  Related Topics 记忆化搜索 数学 动态规划 👍 297 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numWays(self, n: int) -> int:
        '''
        Time: O(log(N)), Space: O(1)
        f[i]: 表示跳上一个 n 级的台阶总共有f[i]种跳法
        转移： f[i] = f[i-1] + f[i-2], 最后一阶是跳上一阶 OR 跳上2阶
        初始状态：f[0] = 1, f[1]=1， f[2]=2
        example:
            i=0: {1, 1, 2}
            i=1: {1, 2, 3}
            i=2: {2, 3, 5}
            i=3: {3, 5, 8}
            上一状态：{a, b, c}, 下一状态：{b, c, b+c}, 此方法可把i=0, i=1, 纳入循环之中，不用单独考虑
        '''

        a, b, c = 1, 1, 2
        for i in range(1, n + 1):
            a = b
            b = c
            c = a + b
        return a % 1000000007
# leetcode submit region end(Prohibit modification and deletion)
