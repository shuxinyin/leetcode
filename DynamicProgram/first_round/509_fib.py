'''
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
'''


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1

        for i in range(n):
            tmp = a
            a = b
            b = tmp + b
        return a
