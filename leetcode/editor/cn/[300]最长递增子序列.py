# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。 
# 
#  子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子
# 序列。 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2500 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗? 
#  
#  Related Topics 数组 二分查找 动态规划 👍 2630 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        '''DP
        状态：dp[i] 表示以nums[i]结尾的最长增长子序列最大长度
        转移： if nums[i] > nums[j]:
                dp[i] = dp[j] +1
              else nums[i] <= nums[j]:
                continue
        综合起来： dp[i] = max(dp[i], dp[j] +1)  for j in [0, i)
        初始化： dp[i] 所有元素置 1，含义是每个元素都至少可以单独成为子序列，此时长度都为1
        返回值: max(dp)
        Time: O(N^2)
        Space: O(N)
        '''
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS_DoubleDevided(self, nums: [int]) -> int:
        '''
        状态：tails[i] 表示长度为i+1的子序列尾部元素的值
        如 [1,4,6]序列，长度为 1,2,3的子序列尾部元素值分别为 tails=[1,4,6]
        转移：
        1. 区间中存在 tails[i]>nums[k]： 将第一个满足 tails[i]>nums[k] 执行 tails[i]=nums[k]；因为更小的 nums[k] 后更可能接一个比它大的数字。
        2. 区间中不存在 tails[i]>nums[k]： 意味着 nums[k] 可以接在前面所有长度的子序列之后，因此肯定是接到最长的后面（长度为 res），新子序列长度为 res+1。

        综合起来：
        初始化： dp[i] 所有元素置 1，含义是每个元素都至少可以单独成为子序列，此时长度都为1
        返回值:
        Time: O(NlogN)
        Space: O(N)
        '''
        # Dynamic programming + Dichotomy.
        tails = [0] * len(nums)  #
        res = 0  # tails长度， 最长上升子子序列长度
        for num in nums:
            i, j = 0, res
            print(num, i, j)
            while i < j:  # 二分查找num 寻找插入tails的位置i，保持tails单调增
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 1. 存在 tails[i]>nums[k], i永远是表示大于num的下一个数的index
                else:
                    j = m  # 2.不存在 tails[i]>nums[k], res+1
            print(i, j)
            tails[i] = num
            print(i, j, tails)

            if j == res:
                res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    S = Solution()
    nums = [10, 9, 2, 5, 3, 7, 21, 18]
    print(S.lengthOfLIS_DoubleDevided(nums))
