# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  nums 中的所有元素 互不相同 
#  
#  Related Topics 位运算 数组 回溯 👍 1491 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 方法一
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    # 方法二
    def subsets2(self, nums):
        res = []
        n = len(nums)

        def helper(i, n, tmp):
            res.append(tmp)
            # print(f"{i},,{tmp},,{res}")
            for j in range(i, n):
                helper(j + 1, n, tmp + [nums[j]])

        helper(0, n, [])
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1, 2, 3]
    out = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    S = Solution()
    print(S.subsets(nums))
