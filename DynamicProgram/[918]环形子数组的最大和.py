# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。 
# 
#  环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个
# 元素是 nums[(i - 1 + n) % n] 。 
# 
#  子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不
# 存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 3 * 10⁴ 
#  -3 * 10⁴ <= nums[i] <= 3 * 10⁴ 
#  
#  Related Topics 队列 数组 分治 动态规划 单调队列 👍 373 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubarraySumCircular(self, nums: [int]) -> int:
        '''第一种情况：这个最大连续子数组不是环状的，就是说首尾不相连。
            第二种情况：这个最大连续子数组一部分在首部，一部分在尾部。
            我们可以将这第二种情况转换成第一种情况，那中间的一定是连续的，且是最小子数组和，
            因此最大的环形子数组和 = max(最大子数组和，数组总和-最小子数组和)
            基于以上，就转化成了53题最大字数组和)
        '''
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, n):
            # 最大的连续子集和
            dp_max[i] = max(nums[i], dp_max[i - 1] + nums[i])

            # 最小的连续子集和
            dp_min[i] = min(nums[i], dp_min[i - 1] + nums[i])

        max_sum = max(dp_max)
        min_sum = min(dp_min)
        return max(max_sum, sum(nums) - min_sum) if max_sum > 0 else max_sum

    def maxSubarraySumCircular2(self, nums: [int]) -> int:
        # 由于状态转移方程中，dp[i]只和 dp[i - 1] 有关，可以使用滚动变量方式进行优化
        total, n = 0, len(nums)
        maxSum, curMax = nums[0], 0
        minSum, curMin = nums[0], 0

        for i in range(n):
            # 最大的连续子集和
            curMax = max(nums[i], curMax + nums[i])
            maxSum = max(maxSum, curMax)

            # 最小的连续子集和
            curMin = min(nums[i], curMin + nums[i])
            minSum = min(minSum, curMin)

            total += nums[i]
        # 如果全是负数，那么maxSum就会是负数，总和total就会等于最小和minSum。不这么判断的话，返回值就会是0，实际应该直接返回maxSum
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    S = Solution()
    nums = [9, -4, -7, 9]
    print(S.maxSubarraySumCircular(nums))
    print(S.maxSubarraySumCircular2(nums))
