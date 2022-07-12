# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 19 
#  
#  Related Topics 树 二叉搜索树 数学 动态规划 二叉树 👍 1827 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        转移式:  f(i) 为以 i 为根的二叉搜索树的个数，则 C(i)=f(1)+f(2)+f(3)+f(4)+...+f(i)
                C(i) = C(0)∗C(i−1) + C(1)∗(i−2) +...+ C(i−1)∗C(0)
        '''
        dp = [1] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j-1] * dp[i - j]

        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
