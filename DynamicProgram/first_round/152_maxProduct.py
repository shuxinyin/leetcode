class Solution:
    def maxProduct(self, nums: [int]) -> int:

        n = len(nums)
        max_value = float("-inf")
        imax, imin = 1, 1
        for i in range(n):
            if nums[i] < 0:
                tmp = imax
                imax = imin
                imin = tmp

            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])

            max_value = max(max_value, imax)

        return max_value


if __name__ == '__main__':
    nums = [-2, 3, -4]
    S = Solution()
    print(S.maxProduct(nums))
