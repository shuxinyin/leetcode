# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。 
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: prices = [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#  
# 
#  示例 2: 
# 
#  
# 输入: prices = [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#  
# 
#  示例 3: 
# 
#  
# 输入: prices = [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 3 * 10⁴ 
#  0 <= prices[i] <= 10⁴ 
#  
#  Related Topics 贪心 数组 动态规划 👍 1496 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices):
        '''只执行n次交易
        「贪心算法」 和 「动态规划」、「回溯搜索」 算法一样，完成一件事情，是 分步决策 的；
        「贪心算法」 在每一步总是做出在当前看来最好的选择，我是这样理解 「最好」 这两个字的意思：
        「最好」 的意思往往根据题目而来，可能是 「最小」，也可能是 「最大」；
        贪心算法和动态规划相比，它既不看前面（也就是说它不需要从前面的状态转移过来），也不看后面（无后效性，后面的选择不会对前面的选择有影响），
        因此贪心算法时间复杂度一般是线性的，空间复杂度是常数级别的；
        这道题 「贪心」 的地方在于，对于 「今天股价-昨天股价」，得到的结果有 3 种可能：① 正数，② 0，③负数。贪心算法的决策是： 只加正数 。
        Time: O(N)
        Space: O(1)
        '''
        if len(prices) < 2:
            return 0

        diff_sum = 0
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                diff_sum += diff
        return diff_sum
# leetcode submit region end(Prohibit modification and deletion)
