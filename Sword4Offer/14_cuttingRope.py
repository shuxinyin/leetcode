class Solution:

    def cuttingRope_greedy(self, n: int) -> int:
        import math
        if n <= 3:
            return n - 1

        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))  # 最后一段取3
        if b == 1:
            return int(math.pow(3, a - 1) * 4)  # 最后一段取4

        return int(math.pow(3, a) * 2)  # 最后一段取2

    def cuttingRope_dp(self, n: int) -> int:
        '''
        dp五部曲:
        1.状态定义:dp[i]为长度为i的绳子剪成m段最大乘积为dp[i]
        2.状态转移:dp[i]有两种途径可以转移得到
            2.1 由前面某一个dp[j]*(i-j)得到,即前面剪了>=2段,后面再剪一段,此时的乘积个数>=3个
            2.2 前面单独成一段,后面剩下的单独成一段,乘积为j*(i-j),乘积个数为2
            两种情况中取大的值作为dp[i]的值,同时应该遍历所有j,j∈[1,i-1],取最大值
        3.初始化:初始化dp[1]=1即可
        4.遍历顺序:显然为正序遍历
        5.返回坐标:返回dp[n]
        '''
        dp = [1 for _ in range(n + 1)]
        dp[1] = 1
        #  遍历[2,n]的每个状态
        for i in range(2, n + 1):
            for j in range(1, i):
                tmp = max(dp[j] * (i - j), j * (i - j))
                dp[i] = max(tmp, dp[i])

        return dp[n]
