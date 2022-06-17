# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。 
# 
#  你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。 
# 
#  请你计算并返回达到楼梯顶部的最低花费。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：cost = [10,15,20]
# 输出：15
# 解释：你将从下标为 1 的台阶开始。
# - 支付 15 ，向上爬两个台阶，到达楼梯顶部。
# 总花费为 15 。
#  
# 
#  示例 2： 
# 
#  
# 输入：cost = [1,100,1,1,1,100,1,1,100,1]
# 输出：6
# 解释：你将从下标为 0 的台阶开始。
# - 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
# - 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
# - 支付 1 ，向上爬一个台阶，到达楼梯顶部。
# 总花费为 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= cost.length <= 1000 
#  0 <= cost[i] <= 999 
#  
#  Related Topics 数组 动态规划 👍 923 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        ''' DP
        状态： dp[i]表示到达第i阶台阶顶部的最小花费（越过第i阶）
        转移： dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i-1]), min(爬一步， 爬两步)
        初始状态： dp[0]=0,表示从地面开始
         dp[1] = min(cost[0], cost[1])表示从第0阶顶部开始或从1阶顶部开始
        '''
        n = len(cost)
        dp = [0] * n
        dp[1] = min(cost[0], cost[1])

        for i in range(2, n):
            print(dp)
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i - 1])
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    cost = [10, 15, 20]
    S = Solution()
    print(S.minCostClimbingStairs(cost))
