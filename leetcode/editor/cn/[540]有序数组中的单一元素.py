# 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。 
# 
#  请你找出并返回只出现一次的那个数。 
# 
#  你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,2,3,3,4,4,8,8]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: nums =  [3,3,7,7,10,11,11]
# 输出: 10
#  
# 
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 二分查找 👍 471 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNonDuplicate(self, nums):
        '''
        由于给定数组有序 且 常规元素总是两两出现，因此如果不考虑“特殊”的单一元素的话，
        有结论：成对元素中的第一个所对应的下标必然是偶数，成对元素中的第二个所对应的下标必然是奇数。
        然后再考虑存在单一元素的情况，假如单一元素所在的下标为 xxx，那么下标 xxx 之前（左边）的位置仍满足上述结论，
        而下标 xxx 之后（右边）的位置由于 xxx 的插入，导致结论翻转。

        利用按位异或的性质，可以得到mid和相邻的数之间的如下关系，其中 ⊕是按位异或运算符：
        当mid是偶数时，mid+1=mid⊕1；
        当mid是奇数时，mid−1=mid⊕1。  因此在二分查找的过程中，不需要判断 mid的奇偶性
        '''

        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == nums[mid ^ 1]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

    def singleNonDuplicate2(self, nums):
        '''
        常规方法
        '''
        n = len(nums)
        l, r = 0, n - 1

        for i in range(n):
            if i % 2 == 0:
                if nums[i] == nums[i + 1]:
                    continue
                else:
                    return nums[i]

            # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [3, 3, 7, 7, 10, 11, 11]
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    S = Solution()
    print(S.singleNonDuplicate(nums))
