# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。 
# 
#  返回 你可以获得的最大乘积 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。 
# 
#  示例 2: 
# 
#  
# 输入: n = 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。 
# 
#  
# 
#  提示: 
# 
#  
#  2 <= n <= 58 
#  
#  Related Topics 数学 动态规划 👍 863 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        状态： dp[i]表示正整数i 拆分成至少两个正整数的和之后，这些正整数的最大乘积
        转移： dp = max(dp[i], j * (i - j), j * dp[i - j])
        - 将 i 拆分成 j 和 i−j的和，且 i−j不再拆分成多个正整数，此时的乘积是 j×(i−j)；
        - 将 i 拆分成 j 和 i−j的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j×dp[i−j]。

        '''
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # 存在这种情况： 4 = 1 + 1 + 1 + 1
            dp[i] = i

            for j in range(1, i):
                dp = max(dp[i], j * (i - j), j * dp[i - j])
            return dp[-1]


class Solution2:
    def integerBreak(self, n: int) -> int:
        '''
        ① 当所有拆分出的数字相等时，乘积最大。
            a+b >= n*sqrt_n(ab), 当且仅当a==b成立
        ② 最优拆分数字为 3 。
        最优： 3 。把数字 n 可能拆为多个因子 3 ，余数可能为 0,1,20,1,20,1,2 三种情况。
        次优： 2 。若余数为 2 ；则保留，不再拆为 1+1 。
        最差： 1 。若余数为 1 ；则应把一份 3+1 替换为 2+2，因为 2×2>3×1。
        Time: O(1), Space: O(1)
        '''
        import math
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

# leetcode submit region end(Prohibit modification and deletion)
