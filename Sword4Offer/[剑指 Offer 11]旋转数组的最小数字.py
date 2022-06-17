# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
# 
#  给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3
# ,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。 
# 
#  注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], 
# ..., a[n-2]] 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：numbers = [3,4,5,1,2]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：numbers = [2,2,2,0,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == numbers.length 
#  1 <= n <= 5000 
#  -5000 <= numbers[i] <= 5000 
#  numbers 原来是一个升序排序的数组，并进行了 1 至 n 次旋转 
#  
# 
#  注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-
# sorted-array-ii/ 
#  Related Topics 数组 二分查找 👍 640 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minArray(self, numbers: [int]) -> int:
        '''
        为什么本题二分法不用 nums[m] 和 nums[l] 作比较？
        对于以下两示例，当 i=0,j=4,m=2时，有 nums[m] > nums[i] ，而结果不同。
        [1, 2, 3, 4 ,5]旋转点 x=0： m 在右排序数组（此示例只有右排序数组）；
        [3, 4, 5, 1 ,2] 旋转点 x=3： m在左排序数组。
        '''
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            mid = l + (r - l) // 2

            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                # 当出现nums[m] = nums[r]时，一定有区间[l, m]内所有元素相等或区间[m, r]内所有元素相等（或两者皆满足）
                r -= 1
        return numbers[l]
# leetcode submit region end(Prohibit modification and deletion)
