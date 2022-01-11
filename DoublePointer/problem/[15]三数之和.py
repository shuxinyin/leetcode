# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 双指针 排序 👍 4133 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums):
        '''
        Sort + Double_Pointer
        1.数组从小到大排序
        2.遍历数组（k），取l，r两个滑动指针， k<l<r
        3.取s=nums[k]+nums[l]+nums[r]
        4.while(l<r)分3类：
            a.s<0: l++
            b.s>0: r--
            c.s==0: 添加此组合（k,l,r）, l,r继续滑动，寻找还有没有其他结果
        '''
        nums = sorted(nums)
        res = []
        for k in range(len(nums) - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k - 1]: continue
            l, r = k + 1, len(nums) - 1
            while l < r:
                print(l, r)
                tmp = nums[k] + nums[l] + nums[r]
                if tmp < 0:
                    l += 1
                    # 重复的值跳过
                    while l < r and nums[l] == nums[l - 1]: l += 1
                elif tmp > 0:
                    r -= 1
                    # 重复的值跳过
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                else:
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 重复的值跳过
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    S = Solution()
    l = [-1, 0, 1, 2, -1, -4]
    print(S.threeSum(l))
