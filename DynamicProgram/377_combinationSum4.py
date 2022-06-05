class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        # 内外循环交换
        for i in range(1, target + 1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i - n]
            # print(dp)
        return dp[-1]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    nums = [9]
    target = 3
    S = Solution()
    print(S.combinationSum4(nums, target))
