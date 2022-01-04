# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[
# b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： 
# 
#  
#  0 <= a, b, c, d < n 
#  a、b、c 和 d 互不相同 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  你可以按 任意顺序 返回答案 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics 数组 双指针 排序 👍 1055 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)

        res = []
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # 当i的值与前面的值相等时忽略
                continue
            # 获取当前最小值,如果最小值比目标值大,说明后面越来越大的值根本没戏
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break  # 这里使用的break,直接退出此次循环,因为后面的数只会更大
            # 获取当前最大值,如果最大值比目标值小,说明后面越来越小的值根本没戏,忽略
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue  # 这里使用continue,继续下一次循环,因为下一次循环有更大的数

            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # 当j的值与前面的值相等时忽略
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue

                l, r = j + 1, length - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                        # 去重复值，跳过
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s > target:
                        r -= 1
                        # 去重复值，跳过
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # 去重复值，跳过
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # l = [1, 0, -1, 0, -2, 2]
    # target = 0
    l = [2, 2, 2, 2, 2]
    target = 8
    S = Solution()
    print(S.fourSum(l, target))
