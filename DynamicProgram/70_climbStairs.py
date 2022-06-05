class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, c = 0, 0, 1

        for i in range(1, n+1):
            a = b
            b = c
            c = a + b
        return c