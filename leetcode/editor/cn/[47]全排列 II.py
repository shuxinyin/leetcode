# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics 数组 回溯 👍 952 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums):
        if not nums:
            return

        res = []
        nums.sort()
        n = len(nums)
        visited = [0] * n

        def helper1(temp_list, length):
            if length == n:
                res.append(temp_list)
            for i in range(n):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = 1
                helper1(temp_list + [nums[i]], length + 1)
                visited[i] = 0

        helper1([], 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums = [1, 1, 2]
    S = Solution()
    res = S.permuteUnique(nums)
    print(res)
