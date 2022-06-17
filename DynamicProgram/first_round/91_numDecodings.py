class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0' or '00' in s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[-1] = 1, 1

        # dp[1] =1 if s[0]>'2' else 2

        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                if 10 < int(s[i - 1:i + 1]) < 27:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        # 由于dp最后一位初始化为 1，所以返回 dp的倒数第二个
        return dp[-2]


if __name__ == '__main__':
    S = Solution()
    print(S.numDecodings("2101"))