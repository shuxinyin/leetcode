class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 类似题300的解答
        # 状态：up[i]表示以i结尾的最长向上摆动序列
        if not nums:
            return 0

        n = len(nums)
        up = [1 for _ in range(n)]
        down = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
        return max(max(up), max(down))


class Solution2:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 换一种dp状态定义
        # 状态：up[i]表示前i个元素中的最长向上摆动序列长度
        if not nums:
            return 0

        n = len(nums)
        up = [1 for _ in range(n)]
        down = [1 for _ in range(n)]

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(down[i - 1] + 1, up[i - 1])
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = max(up[i - 1] + 1, down[i - 1])
                up[i] = up[i - 1]

            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n - 1], down[n - 1])

    def wiggleMaxLength_optimize(self, nums: List[int]) -> int:
        # 贪心算法
        n = len(nums)
        if n < 2:
            return n

        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(up, down)
