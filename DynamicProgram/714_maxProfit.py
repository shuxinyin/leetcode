class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit

    def maxProfit_122(self, prices: [int], fee: int) -> int:
        '''
        122 题解
        '''
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:  # 表明应该在此时 以更低的价格买入
                buy = prices[i]
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit


if __name__ == '__main__':
    nums = [1, 3, 2, 8, 4, 9]
    S = Solution()
    print(S.maxProfit(nums, 2))
