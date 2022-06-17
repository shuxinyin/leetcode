class Solution:
    def integerBreak(self, n: int) -> int:
        # dp法
        # Time: O(n^2)
        # Space: O(n)
        dp = [0] * (n + 1)
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]

    def integerBreak_math(self, n):
        # math solution
        # 2个推导：① 当所有拆分出的数字相等时，乘积最大。
        #        ② 最优拆分数字为3， b=n%3:
        #             1. b=0时, 返回3^a
        #             2. b=1时, 1+3 -> 2+2 返回3^(a-1) * 4
        #             3. b=2时, 返回3^a*2
        import math
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        elif b == 1:
            return int(math.pow(3, a - 1) * 4)
        else:
            return int(math.pow(3, a) * 2)

