class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):  # 只到倒数第二个位置n-2，nums[n-2]>0,则ok(return处判断)
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])

                if i == end:
                    end = maxPos
                    step += 1

        return step
