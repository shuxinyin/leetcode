class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 假设m=3, 首先最后肯定剩下一个数为x，下标为0
        # 倒数第二轮，剩下2个数， 此时x位置下标为（0+3）%2=1
        # 以此倒推就得(当前index + m) % 上一轮剩余数字的个数

        ans = 0
        for i in range(2, n + 1):
            ans = (ans + m) % i
        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.lastRemaining(5, 3))
