class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        定义状态：dp[i]表示从nums[0]到nums[i]且以nums[i]为结尾的等差数列子数组的数量。
        状态转移方程：dp[i] = dp[i-1]+1 if nums[i]-nums[i-1]==nums[i-1]-nums[i-2] else 0
        解释：如果nums[i]能和nums[i-1]nums[i-2]组成等差数列，则以nums[i-1]结尾的等差数列均可以nums[i]结尾，
            且多了一个新等差数列[nums[i],nums[i-1],nums[i-2]]
        '''
        n = len(nums)
        dp = [0] * n
        for i in range(2, n):
            dp[i] = dp[i - 1] + 1 if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2] else 0
        return sum(dp)

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
            差分 + 计数
        '''
        n = len(nums)
        if n == 1:
            return 0

        d, t = nums[0] - nums[1], 0
        ans = 0

        # 因为等差数列的长度至少为 3，所以可以从 i=2 开始枚举
        for i in range(2, n):
            if nums[i - 1] - nums[i] == d:
                t += 1
            else:
                d = nums[i - 1] - nums[i]
                t = 0
            ans += t

        return ans

