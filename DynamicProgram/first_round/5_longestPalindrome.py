class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp方法
        # Time: O(n^2)
        # Space: O(n^2)

        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                j = L + i - 1
                # 右边界越界，退出循环
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文
                # 此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


# 中心扩展方法：本质为枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止
class SolutionCenter:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        # Time: O(n^2)
        # Space: O(1)

        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1

            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]


# Manacher算法(马拉车算法)
class SolutionManacher:

    def longestPalindrome(self, s: str) -> str:
        pass
    