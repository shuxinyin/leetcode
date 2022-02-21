# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。 
# 
#  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], 
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,
# 2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。 
# 
#  给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 
# target ，则返回 true ，否则返回 false 。 
# 
#  你必须尽可能减少整个操作步骤。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,5,6,0,0,1,2], target = 0
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,5,6,0,0,1,2], target = 3
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -10⁴ <= nums[i] <= 10⁴ 
#  题目数据保证 nums 在预先未知的某个下标上进行了旋转 
#  -10⁴ <= target <= 10⁴ 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  这是 搜索旋转排序数组 的延伸题目，本题中的 nums 可能包含重复元素。 
#  这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？ 
#  
# 
#  
#  Related Topics 数组 二分查找 👍 543 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums, target):
        '''
        将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
        此时有序部分用二分法查找。
        无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
        '''
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2  # [0:mid], [mid+1, r]
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:  # 左边[0:mid],有序
                if nums[0] <= target < nums[mid]:  # target 只
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # 右边[mid+1, r],有序
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0

    S = Solution()
    print(S.search(nums, target))
