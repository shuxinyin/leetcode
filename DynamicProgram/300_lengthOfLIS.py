class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

    def lengthOfLIS_optimize(self, nums: List[int]) -> int:
        # Dynamic programming + Dichotomy.
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:  # 二分查找num 插入tails的位置，保持tails单调增
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            if j == res:
                res += 1
        return res
