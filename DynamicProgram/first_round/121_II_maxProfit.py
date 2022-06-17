class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit

    def maxProfit_122(self, prices: [int], fee: int) -> int:

        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:  # 表明应该在此时 以更低的价格买入
                buy = prices[i]
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit
