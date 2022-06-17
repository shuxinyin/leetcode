class Solution:
    def canJump(self, nums: [int]) -> bool:

        end = 0
        n = len(nums)

        for i in range(n - 1):  # 只到倒数第二个位置n-2，nums[n-2]>0,则ok(return处判断)
            step = nums[i]

            if i > end:  # 说明最远end到不了位置i,直接返回false
                return False
            # jy: 基于当前能走的最大步数更新至今能走到的最远位置;
            end = max(end, i + step)

        return end >= n - 1
