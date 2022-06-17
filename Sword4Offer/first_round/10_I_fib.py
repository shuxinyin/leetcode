class Solution:
    def fib(self, n: int) -> int:
        # Time: O(log(N)), Space: O(1)
        a, b = 0, 1
        for _ in range(n):
            tmp = a
            a = b
            b = tmp + b
        return a % 1000000007


if __name__ == '__main__':
    n = 37
    S = Solution()
    print(S.fib(n))
