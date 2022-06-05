class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # Time: O(N), Space: O(N)
        set_nums = set()

        for n in nums:
            if n in set_nums:
                return n
            else:
                set_nums.add(n)
