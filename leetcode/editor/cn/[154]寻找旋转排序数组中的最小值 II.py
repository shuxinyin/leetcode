# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变
# 化后可能得到：
#  
#  若旋转 4 次，则可以得到 [4,5,6,7,0,1,4] 
#  若旋转 7 次，则可以得到 [0,1,4,4,5,6,7] 
#  
# 
#  注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], 
# ..., a[n-2]] 。 
# 
#  给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,3,5]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,0,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 5000 
#  -5000 <= nums[i] <= 5000 
#  nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  这道题是 寻找旋转排序数组中的最小值 的延伸题目。 
#  允许重复会影响算法的时间复杂度吗？会如何影响，为什么？ 
#  
#  Related Topics 数组 二分查找 👍 452 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums):
        # nums可能存在重复元素值的数组
        '''
        最小值只存在两种情况，
        一种存在于左边， 则 r = mid
        一种存在于右边， 则 l = mid + 1
        一种nums[mid]=nums[l]=nums[r], 则r-=1, 因为nums[r]可被nums[mid]替代
        '''
        n = len(nums)
        l, r = 0, n

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:  # 说明最小元素在[l, mid]
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1  # 说明最小元素在[mid, r]
            else:
                r = r - 1
        return nums[l]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    nums = [2, 2, 2, 0, 1]
    S = Solution()
    print(S.findMin(nums))
