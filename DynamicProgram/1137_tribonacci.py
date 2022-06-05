'''
泰波那契序列 Tn 定义如下： 
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
'''


class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1

        for _ in range(n):
            tmp1, tmp2 = a, b
            a = b
            b = c
            c += tmp1 + tmp2
        return a


if __name__ == '__main__':
    S = Solution()
    print(S.tribonacci(4))