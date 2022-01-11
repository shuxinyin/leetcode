# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 
#  返回这三个数的和。 
# 
#  假定每组输入只存在恰好一个解。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,0], target = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics 数组 双指针 排序 👍 988 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums, target):
        '''
        Sort + Double_Pointer
        1. 首先定义res-target无限大，第一步让res等于第一个组合的sum
        2. 剩下就分为三类情况，
            2.1 sum < target: l+=1
            2.1 sum > target: r-=1
            2.1 sum = target: return sum
        '''
        nums = sorted(nums)
        res = float("inf")
        for k in range(len(nums) - 2):
            l, r = k + 1, len(nums) - 1
            while l != r:
                tmp = nums[l] + nums[k] + nums[r]
                if abs(res - target) >= abs(tmp - target):
                    res = tmp
                if tmp - target < 0:
                    l += 1
                    # nums[left]重复值，则跳过
                    while l != r and nums[l] == nums[l - 1]:
                        l += 1
                elif tmp - target > 0:
                    r -= 1
                    # nums[right]重复值，则跳过
                    while l != r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    return tmp

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    l = [0, 2, 1, -3]  # 【-3， 0， 1 ，2】
    l2 = [-1, 2, 1, -4]
    target = 1
    l3 = [1, 1, -1, -1, 3]
    target3 = 1
    S = Solution()
    print(S.threeSumClosest(l3, target3))
