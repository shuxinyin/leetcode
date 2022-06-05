# 前缀问题  1314前篇  https://www.bilibili.com/video/BV19J41147jQ?spm_id_from=333.337.search-card.all.click
class Solution:
    def matrixBlockSum(self, mat: [[int]], threshold: int) -> [[int]]:
        # Time: O(m * n * min(m, n))
        # Space: O(m * n)
        m, n = len(mat), len(mat[0])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for y in range(1, m + 1):
            for x in range(1, n + 1):
                dp[y][x] = dp[y][x - 1] + dp[y - 1][x] - dp[y - 1][x - 1] + mat[y - 1][x - 1]

        def rangeSum(x1, y1, x2, y2):
            return dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 - 1][x1 - 1]

        ans = 0
        for y in range(1, m + 1):
            for x in range(1, n + 1):
                k = 0
                while y + k <= m and x + k <= n:
                    res = rangeSum(x, y, x + k, y + k)
                    if res > threshold:
                        break
                    ans = max(ans, k + 1)
                    k += 1

        return ans

    # Solution Bounded Search
    def matrixBlockSum_bound(self, mat: [[int]], threshold: int) -> [[int]]:
        # Time: O(m * n + min(m, n))
        # Space: O(m * n)
        m, n = len(mat), len(mat[0])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for y in range(1, m + 1):
            for x in range(1, n + 1):
                dp[y][x] = dp[y][x - 1] + dp[y - 1][x] - dp[y - 1][x - 1] + mat[y - 1][x - 1]

        def rangeSum(x1, y1, x2, y2):
            return dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 - 1][x1 - 1]

        ans = 0
        for y in range(1, m + 1):
            for x in range(1, n + 1):
                k = ans  # changed here
                while y + k <= m and x + k <= n:
                    res = rangeSum(x, y, x + k, y + k)
                    if res > threshold:
                        break
                    ans = max(ans, k + 1)
                    k += 1

        return ans

    # Solution Bounded Search
    def matrixBlockSum_bound(self, mat: [[int]], threshold: int) -> [[int]]:
        # Time: O(m * n + min(m, n))
        # Space: O(m * n)
        m, n = len(mat), len(mat[0])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for y in range(1, m + 1):
            for x in range(1, n + 1):
                dp[y][x] = dp[y][x - 1] + dp[y - 1][x] - dp[y - 1][x - 1] + mat[y - 1][x - 1]

        def rangeSum(x1, y1, x2, y2):
            return dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 - 1][x1 - 1]

        ans = 0
        for y in range(1, m + 1):
            for x in range(1, n + 1):
                k = ans  # changed here
                while y + k <= m and x + k <= n:
                    res = rangeSum(x, y, x + k, y + k)
                    if res > threshold:
                        break
                    ans = max(ans, k + 1)
                    k += 1

        return ans


if __name__ == '__main__':
    mat = [[1, 1, 3, 2, 4, 3, 2],
           [1, 1, 3, 2, 4, 3, 2],
           [1, 1, 3, 2, 4, 3, 2]]
    threshold = 4

    S = Solution()
    print(S.matrixBlockSum(mat, threshold))
