# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
#  请必须使用时间复杂度为 O(log n) 的算法。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
#  
# 
#  示例 3: 
# 
#  
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
#  
# 
#  示例 4: 
# 
#  
# 输入: nums = [1,3,5,6], target = 0
# 输出: 0
#  
# 
#  示例 5: 
# 
#  
# 输入: nums = [1], target = 0
# 输出: 0
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 为无重复元素的升序排列数组 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics 数组 二分查找 👍 1286 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            print(l, r)
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target == nums[r]:
                return r

            elif nums[l] < target < nums[mid]:
                r = mid - 1
            elif nums[mid] < target < nums[r]:
                l = mid + 1
            elif target <= nums[l]:
                return l
            else:
                return r + 1
        return l + 1

    def searchInsert2(self, nums, target):

        left = 0, len(nums) - 1
        ans = len(nums)  # target > nums[r]情形
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    S = Solution()
    nums = [1, 3, 5, 6]
    t = 5
    t = 2
    t = 7
    print(S.searchInsert(nums, t))
