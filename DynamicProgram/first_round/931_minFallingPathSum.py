class Solution:
    def minFallingPathSum(self, matrix: [[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [0] * (n + 2)  # 处理选择左下或者右下会出现越界的情况。
        f[0], f[n + 1] = float("inf"), float("inf")

        for j in range(1, n + 1):
            f[j] = matrix[0][j - 1]

        for i in range(1, m):  # BEGIN FROM ROW 1
            last = float("inf")
            for j in range(1, n + 1):
                temp = f[j]  # 保留的是左上角的值，因为dp过后更新了要存一下
                f[j] = matrix[i][j - 1] + min(min(last, f[j]), f[j + 1])
                last = temp

        min_value = float("inf")
        for j in range(1, n+1):
            min_value = min(min_value, f[j])
        return min_value


if __name__ == '__main__':
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    S = Solution()
    print(S.minFallingPathSum(matrix))