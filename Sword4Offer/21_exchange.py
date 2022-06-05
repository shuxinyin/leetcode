class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # Time: O(N), Space: O(1)
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1:
                i += 1
            while i < j and nums[i] & 1 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

    def exchange_deque(self, nums: List[int]) -> List[int]:
        # Time: O(N), Space: O(N)
        # 双边队列  奇数放对头，偶数放对尾
        import collections
        tmp = collections.deque()
        for n in nums:
            tmp.append(n) if n & 1 == 1 else tmp.append(n)
        return list(tmp)
