class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res用来存放结果
        if not nums:
            return []
        res = []
        used = [0] * len(nums)

        def backtracking(nums, used, path):
            # 终止条件
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtracking(nums, used, path)
                    path.pop()
                    used[i] = 0

        # 记得给nums排序
        backtracking(sorted(nums), used, [])
        return res
