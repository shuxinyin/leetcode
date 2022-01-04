# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。 
# 
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。 
# 
#  必须 原地 修改，只允许使用额外常数空间。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 100 
#  
#  Related Topics 数组 双指针 👍 1461 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.

        标准的“下一个排列”算法可以描述为：
        1. 从后向前查找第一个相邻升序的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序
        2. 在 [j,end) 从后向前查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」
        将 A[i] 与 A[k] 交换
        3. 可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序
        4. 如果在步骤 1 找不到符合的相邻元素对，说明当前 [begin,end) 为一个降序顺序，则直接跳到步骤 4
        """
        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1

        #  find: A[i] < A[j]
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0:  # 不是最后一个排列,即不是该序列最大的排列组合
            # find: A[i] < A[k]
            while nums[i] >= nums[k]:
                k -= 1
                #  swap A[i], A[k]
            nums[i], nums[k] = nums[k], nums[i]

        #  reverse  A[j:end]
        i, j = j, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j - 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    S = Solution()
    nums = [1, 2, 3]
    # nums = [3, 2, 1]
    # nums = [1, 3, 2]  # 【2，1，3】
    print(S.nextPermutation(nums))
