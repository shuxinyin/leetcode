# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
# 
#  
# 
#  示例 1: 
# 
#  输入: [0,1,3]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8 
# 
#  
# 
#  限制： 
# 
#  1 <= 数组长度 <= 10000 
#  Related Topics 位运算 数组 哈希表 数学 二分查找 👍 278 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == mid:  # missing number为界，左边的nums[i] == i
                l = mid + 1
            else:     # 右边的nums[i] > i
                r = mid - 1
        return l
# leetcode submit region end(Prohibit modification and deletion)
