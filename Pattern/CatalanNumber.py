# 96 二叉搜索树的个数
class Solution:
    def numTrees(self, n: int) -> int:
        # 卡特兰数  https://www.bilibili.com/video/BV1nE411A7ST?p=1
        dp = [1] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):  # i个节点存在二叉排序树的个数是G(i)
            for j in range(1, i + 1):  # f(j)为以i为根的二叉搜索树的个数
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]
