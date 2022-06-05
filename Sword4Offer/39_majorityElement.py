class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time: O(N)
        # Space: O(1)
        vote, count = 0, 0
        for num in nums:
            if vote == 0:
                x = num
            if num == x:
                vote += 1
            else:
                vote -= 1

        # 验证 x 是否为众数
        for num in nums:
            if num == x: count += 1
        return x if count > len(nums) // 2 else 0  # 当无众数时返回 0
