# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  测试用例的答案是一个 32-位 整数。 
# 
#  子数组 是数组的连续子序列。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数 
#  
#  Related Topics 数组 动态规划 👍 1688 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ''' 求最大乘积，因为负数 * 负数 = 正数，负数乘积imin可能变imax， imax, imin
            转移： imax = max(imax*nums[i], nums[i])
                  imin = min(imin*nums[i], nums[i])
                  max_val = max(imax, imin)
        '''

        n = len(nums)
        max_value = float("-inf")
        imax, imin = 1, 1
        for i in range(n):
            if nums[i] < 0:
                tmp = imax
                imax = imin
                imin = tmp

            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])

            max_value = max(max_value, imax)

        return max_value
# leetcode submit region end(Prohibit modification and deletion)
