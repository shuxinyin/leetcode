class Solution:
    def cuttingRope(self, n: int) -> int:
        # 如果n == 2，返回1
        # 如果n == 3，返回2，两个可以合并成n小于4的时候返回n - 1
        # 如果n == 4，返回4
        # 如果n > 4，分成尽可能多的长度为3的小段，每次循环长度n减去3，乘积res乘以3；最后返回时乘以小于等于4的最后一小段；
        # 每次乘法操作后记得取余就行以上2和3可以合并

        if n < 4:
            return n - 1
        res = 1
        while n > 4:
            res = res * 3 % 1000000007
            n -= 3
        return res * n % 1000000007


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1

        a, b = n // 3 - 1, n % 3
        p, x, rem = 1000000007, 3, 1

        while a > 0:
            if a % 2:
                rem = (rem * x) % p

            x = x ** 2 % p
            a //= 2
        if b == 0:
            return (rem * 3) % p  # = 3^(a+1) % p
        if b == 1:
            return (rem * 4) % p  # = 3^a * 4 % p

        return (rem * 6) % p  # = 3^(a+1) * 2  % p
