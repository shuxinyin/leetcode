## 背包问题

### 1. 0-1背包

###### 1.类似的题目:

> 背包大小为m, 在n个物品中挑选若干物品，第i个物品的大小为w[i], 价值是v[i],
> 每件物品只能选一次，求解将哪些物品装入背包里物品价值总和最大？   
> 输入： weights = [1, 3, 4], values=[15, 20, 30], capacity=4
> 输出： 35

###### 解决方法:

```python
# 1. 状态定义：dp[i][j]:表示前i个物品放入容量为j的背包最大价值。
# 如dp[i-1][j-weights[i]]+values[i] 表示放入第i个时的价值， dp[i-1][j]表示不放入第i个时的价值
# 2. 转移方程： dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]+values[i]]), 第i个物品不加与加两种状态。
# 3. 初始状态： dp[0][j] = 0, dp[i][0] = 0
# 4. 返回： dp[-1][-1]
def backpack(capacity, weights, values):
    N = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(len(N) + 1)]
    for i in range(1, N + 1):
        w, v = weights[i - 1], values[i - 1]
        for j in range(1, capacity + 1):
            if j >= w:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[N][capacity]
```

优化：一维数组，dp[j]相当于是把二维中上一行状态复制下来了

```python
# 1. 状态定义：dp[j]:表示容量为j的背包可配置的最大价值。
# 2. 转移方程： dp[j] = max(dp[j], dp[j-weights[i]+values[i]]), 第i个物品不加与加两种状态。
# 3. 初始状态： dp[0] = 0
# 4. 返回： dp[-1]
# 注意dp[j-w] 表示 dp[i-1][j-w],用到的是二维数组中上一层的状态，所以需要倒序更新，防止正序更新将它覆盖
def backpack(capacity, weights, values):
    N = len(weights)
    # 类似完全背包问题
    dp = [0] * (capacity + 1)
    for i in range(1, N + 1):
        w, v = weights[i - 1], values[i - 1]
        for j in range(capacity, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)

    return dp[-1]
```

### 2. 完全背包

> 背包大小为m, 在n个物品中挑选若干物品，第i个物品的大小为w[i], 价值是v[i],
> **每件物品能选无数次**，求解将哪些物品装入背包里物品价值总和最大？   
> 输入： weights = [1, 3, 4], values=[15, 20, 30], capacity=4
> 输出： 60

```python
# 1. 状态定义：dp[j]:表示容量为j的背包可配置的最大价值。
# 2. 转移方程： dp[j] = max(dp[j], dp[j-weights[i]+values[i]]), 第i个物品不加与加两种状态。
# 3. 初始状态： dp[0] = 0
# 4. 返回： dp[-1]
def backpack(capacity, weights, values):
    N = len(weights)
    # 类似完全背包问题
    dp = [0] * (capacity + 1)
    for i in range(1, N + 1):
        w, v = weights[i - 1], values[i - 1]
        # 正序遍历，前一个状态表示已经加了i物品，当前是第i个物品不加与加两种状态
        for j in range(w, capacity + 1):
            dp[j] = max(dp[j], dp[j - w] + v)

    return dp[-1]
```
###### 1.类似的题目:
[322. 零钱兑换](https://leetcode.cn/problems/coin-change/)
Q: 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。 计算可以凑成总金额所需的 最少的硬币个数

```python
class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        '''与完全背包类似，完全背包求最大价值，这里求物品个数
        二维数组表示：
        状态： dp[i][j]前i种硬币达到金额j的最小硬币数
        转移： dp[i][j] = min(dp[i][j], dp[i][j-coin_i] + 1)

        一维数组表示：
        状态： dp[i]达到金额i的最小硬币数
        转移： dp[i]= min(dp[i], dp[i-coin_i] + 1)
        初始状态：dp[0] = 0， 求最小，其他的值初始化inf
        '''

        N = len(coins)
        # 类似完全背包问题, 求最小，则初始化为inf
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, N + 1):
            w = coins[i - 1]
            # 正序遍历，前一个状态表示已经加了i物品，当前是第i个物品不加与加两种状态
            for j in range(w, amount + 1):
                dp[j] = min(dp[j], dp[j - w]+1)
        return dp[-1] if dp[-1] != float("inf") else -1
```

[518. 零钱兑换 II](https://leetcode.cn/problems/coin-change-2/)
Q:给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。 
计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。 
```python
class Solution:
    def change(self, amount: int, coins: [int]) -> int:
        '''与完全背包类似，完全背包求最大价值，这里求物品个数
        一维数组表示：
        状态： dp[i]达到金额i的硬币组合数
        转移： dp[i] += dp[i - coin[i]]
        初始状态：dp[0] = 1，其他的值初始化0
        '''
        N = len(coins)
        # 类似完全背包问题
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(1, N + 1):
            w = coins[i - 1]
            for j in range(w, amount + 1):
                dp[j] += dp[j - w]
        return dp[-1]
```

### 3. 多重背包

> 背包大小为m, 在n个物品中挑选若干物品，第i个物品的大小为w[i], 价值是v[i],
> **每件物品能选有限次counts[i]**，求解将哪些物品装入背包里物品价值总和最大？   
> 输入： weights = [1, 3, 4], values=[15, 20, 30], counts=[1,2,3], capacity=4
> 输出： 60

一个基本思路是，套用01背包问题求解！  
比如物品1有3个，每个价值为2，复制3个物品1及其价值2，存在数组v和数组w中

```python
def backpack(capacity, weights, values, counts):
    # 转化为01背包
    weight_big, values_big = [], []
    for w, v, n in zip(weights, values, counts):
        weight_big.extend([w] * n)
        values_big.extend([v] * n)

    N = len(weight_big)
    # 类似完全背包问题
    dp = [0] * (capacity + 1)
    for i in range(1, N + 1):
        w, v = weight_big[i - 1], values_big[i - 1]
        for j in range(capacity, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)

    return dp[-1]
```

或者采用三层循环，即在最里层选k个，保证k<=s and k*w<=j

```python
def backpack(capacity, weights, values, counts):
    N = len(weights)
    # 类似完全背包问题
    dp = [0] * (capacity + 1)
    for i in range(1, N + 1):
        w, v, s = weights[i - 1], values[i - 1], counts[i - 1]
        for j in range(capacity, w - 1, -1):
            k = 0
            while k <= s and k * w <= j:
                dp[j] = max(dp[j], dp[j - k * w] + k * v)
                k += 1
    return dp[-1]
```

### 总结一下
都可以采用先遍历数组，在遍历背包容量的方法。
1. 0-1背包问题： 采用一维list动态规划时，遍历背包容量采用倒序遍历
2. 完全背包正序遍历，遍历背包容量采用正序遍历，前一个状态表示已经加了i物品，当前是第i个物品不加与加两种状态
3. 多重背包可转化为0-1背包问题，也就是选取k个物品