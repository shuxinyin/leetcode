class Solution:
    def findNthDigit(self, n: int) -> int:
        '''
        1.所求数位 ① 在某个digit位数中； ② 为从数字start开始的第n个数位。
        2. 所求数位在数字 num 中
        3. 确定所求数位在 num 的哪一数位
        '''
        digit, start, count = 1, 1, 9
        while n > count:  # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit  # 2.
        return int(str(num)[(n - 1) % digit])  # 3.
