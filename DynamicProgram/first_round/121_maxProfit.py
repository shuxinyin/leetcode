class Solution:
    def maxProfit(self, prices: [int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for p in prices:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    S = Solution()
    print(S.maxProfit(prices))