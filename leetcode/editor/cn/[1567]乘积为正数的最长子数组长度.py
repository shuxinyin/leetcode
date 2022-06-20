# 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。 
# 
#  一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。 
# 
#  请你返回乘积为正数的最长子数组长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,-2,-3,4]
# 输出：4
# 解释：数组本身乘积就是正数，值为 24 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,-2,-3,-4]
# 输出：3
# 解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
# 注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。 
# 
#  示例 3： 
# 
#  
# 输入：nums = [-1,-2,-3,0,1]
# 输出：2
# 解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^9 <= nums[i] <= 10^9 
#  
# 
#  
#  Related Topics 贪心 数组 动态规划 👍 162 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaxLen(self, nums: [int]) -> int:
        '''
        状态： pos[i]表示下标i结尾的乘积为正数的最长子数组长度
             neg[i]表示下标i结尾乘积为负数的最长子数组长度。

        转移：i>1时：
                ①. nums[i]>0, 之前的乘积*nums[i]不改变乘积正负性
                    pos[i] = pos[i-1]+1
                    neg[i] = neg[i-1] + 1, if neg[i-1]>0
                    neg[i] = 0, if neg[i-1]=0
                ②. nums[i]<0, 之前的乘积*nums[i]改变乘积正负性
                    pos[i] = neg[i-1]+1, if neg[i-1]>0
                    pos[i] = 0, if neg[i-1]=0
                    neg[i] = pos[i-1] + 1
                ③.当 nums[i]=0时，
                    以下标i结尾的子数组的元素乘积一定为0，因此有 positive[i]=0, negative[i]=0。

        初始状态：i=0: if nums[0] > 0, positive[0] = 1
                    if nums[0] < 0, negative[0] = 1
        '''
        length = len(nums)
        positive, negative = [0] * length, [0] * length
        if nums[0] > 0:
            positive[0] = 1
        elif nums[0] < 0:
            negative[0] = 1

        maxLength = positive[0]
        for i in range(1, length):
            if nums[i] > 0:
                positive[i] = positive[i - 1] + 1
                negative[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
            elif nums[i] < 0:
                positive[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
                negative[i] = positive[i - 1] + 1
            else:
                positive[i] = negative[i] = 0
            maxLength = max(maxLength, positive[i])

        return maxLength

    def getMaxLen2(self, nums: [int]) -> int:
        '''
        滚动数组
        '''
        n = len(nums)
        pos = 1 if nums[0] > 0 else 0
        neg = 1 if nums[0] < 0 else 0

        max_len = pos

        for i in range(1, n):
            if nums[i] > 0:
                pos += 1
                neg = (neg + 1 if neg > 0 else 0)

            elif nums[i] < 0:
                new_pos = (neg + 1 if neg > 0 else 0)
                new_neg = pos + 1
                pos, neg = new_pos, new_neg

            else:
                pos = neg = 0
            max_len = max(max_len, pos)
        return max_len

# leetcode submit region end(Prohibit modification and deletion)
