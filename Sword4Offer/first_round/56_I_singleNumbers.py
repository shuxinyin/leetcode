class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(1)
        n, m = 0, 1
        for num in nums:
            n = n ^ num
        while n & m == 0:  # 找到两个不同数的第一个为1的位置,用于后续分组
            m <<= 1

        x, y = 0, 0
        for num in nums:  # 与m,分成两组,每组只有一个不同的数
            if num & m:
                x ^= num
            else:
                y ^= num
        return x, y
