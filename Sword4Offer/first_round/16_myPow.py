class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        res = 1
        if n < 0:
            x, n = 1 / x, -n

        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.myPow(2, 10))
