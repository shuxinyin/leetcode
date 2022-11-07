### DP-买卖股票问题

#### 1014.最佳观光组合
> 给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。 
>  一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。
>  返回一对观光景点能取得的最高分。 

>  示例 1： 
> 输入：values = [8,1,5,2,6]
> 输出：11
> 解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11


```python
class Solution:
    def maxScoreSightseeingPair(self, nums: List[int]) -> int:
        '''
        dp[j]: 以values[j]结尾的最大得分
        转移： dp[j] = values[i] + i + values[j] - j, i < j, 
        分成两部分: max_pre = values[i] + i, 找到最大这个值
                接着比较values[j] - j， 保持最大的j, 即最大得分。
        初始状态： nums[0] + 0
        '''
        res = 0
        max_pre = nums[0] + 0

        for j in range(1, len(nums)):
            res = max(res, nums[j] - j + max_pre)
            max_pre = max(max_pre, nums[j] + j)
        return res
```



#### 121.买卖股票的最佳时机
> 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。 
>  你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。 
>  返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。 

>  示例 1： 
> 输入：[7,1,5,3,6,4]
> 输出：5
> 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
>      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' 
        '''
        n = len(prices)
        min_price = float('inf')
        res = 0
        for i in range(n):
            res = max(res, prices[i] - min_price)
            min_price = max(min_price, prices[i])
        return res
```


#### 122.买卖股票的最佳时机II

>  给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。  
>  设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。 
>  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
> 
>  示例 1: 
> 输入: prices = [7,1,5,3,6,4]
> 输出: 7
> 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
>      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

```python
class Solution:
    def maxProfit(self, prices):
        ''' 贪心算法： 对于 「今天股价-昨天股价」，得到的结果有 3 种可能：① 正数，② 0，③负数。
            贪心算法的决策是： 只加正数 。
        '''
        n = len(prices)
        if n < 2:
            return 0
        
        res = 0
        for i in range(1, n):
            gap = prices[i] - prices[i-1]

            if gap>0:
                res += gap
        return res
```

#### 123.买卖股票的最佳时机III

>  给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。 
>  设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。 
>  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
> 
> 示例 1: 
> 输入：prices = [3,3,5,0,0,3,1,4]
> 输出：6
> 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
>      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。 


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' 两笔交易
        状态： dp[i][j]
        '''


```

#### 188.买卖股票的最佳时机IV

> 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。 
>  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。 
>  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
> 
> 示例 1： 
> 输入：k = 2, prices = [2,4,1]
> 输出：2
> 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。 

```python
class Solution:
    def maxProfit(self, k: int, prices: [int]) -> int:
        '''只执行有限次交易，k次交易
        所以定义状态转移数组dp[天数][当前是否持股][卖出的次数]为此时获取的利润
        '''
        n = len(prices)
        if n < 2:
            return 0

        # distance = [[[0] * n] * n] * n
        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n)]  # (n, 2, k+1)

        # 初始化第一天的交易情况
        for i in range(k + 1):
            dp[0][0][i] = 0
            dp[0][1][i] = -prices[0]

        for i in range(1, n):
            dp[i][0][0] = 0
            # [第i天][持股][0次卖出] = max([第i-1天][持股][0次卖出], [第i-1天][不持股][0次卖出] 买入 prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][0] - prices[i])
            for j in range(1, k + 1):
                # [第i天][不持股][j次卖出] = max([第i-1天][不持股][j次卖出], [第i-1天][持股][j次卖出] 卖出 prices[i])
                # [第i天][持股][j次卖出] = max([第i-1天][持股][j次卖出], [第i-1天][不持股][j次卖出] 买入 prices[i])
                dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j] + prices[i])
                dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][0][j] - prices[i])

        print(dp)
        return dp[n - 1][0][k]
```




#### 714.买卖股票的最佳时机含手续费
>  给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格；整数 fee 代表了交易股票的手续费用。 
>  你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。 
>  返回获得利润的最大值。 
>  注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。 

> 示例 1： 
> 输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
> 输出：8
> 解释：能够达到的最大利润:  
> 在此处买入 prices[0] = 1
> 在此处卖出 prices[3] = 8
> 在此处买入 prices[4] = 4
> 在此处卖出 prices[5] = 9
> 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8 



```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ''' 执行最少次交易，达到最大利润(买卖股票的最佳时机II)
        这道题「贪心」的地方在于，对于「今天股价-昨天股价」，得到的结果有 3 种可能：① 正数，② 0，③负数。
            把费用归到buy中， buy = prices[i] + fee， 贪心算法的决策是： 只加正数 。
        Time: O(N)
        Space: O(1)
        ''' 
        n = len(prices)
        buy = prices[0] + fee
        profit = 0

        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]  # 若后续碰见比price[i]大的，此时不加fee,直接减，表示上一个price不是最优
        return profit
```