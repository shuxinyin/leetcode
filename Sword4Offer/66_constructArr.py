class Solution:
    def constructArr(self, a: [int]) -> [int]:
        # Time: O(N)
        # Space: O(1)
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]  # 下三角
        for i in range(len(a) - 2, -1, -1):
            print(i)
            tmp *= a[i + 1]  # 上三角
            b[i] *= tmp  # 下三角 * 上三角
        return b


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]

    S = Solution()
    print(S.constructArr(a))

