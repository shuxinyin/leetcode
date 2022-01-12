# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  进阶： 
# 
#  
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics 数组 二分查找 👍 1393 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums, target):
        '''
        考虑 target开始和结束位置，
        其实我们要找的就是数组中「第一个等于 target的位置」（记为leftIdx）
        和「第一个大于 target的位置减一」（记为rightIdx）。
        '''

        def lower_bound(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l

        def upper_bound(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > target:  # upper bound 寻找的第一个大于target的位置
                    r = mid
                else:
                    l = mid + 1
            return l

        low_bound = lower_bound(nums, target)
        up_bound = upper_bound(nums, target) - 1
        if low_bound == len(nums) or nums[low_bound] != target:
            return [-1, -1]
        else:
            return [low_bound, up_bound]

# leetcode submit region end(Prohibit modification and deletion)
