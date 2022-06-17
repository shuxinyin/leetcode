class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time: O(logN)
        # Space: O(1)
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.hammingWeight(11))
