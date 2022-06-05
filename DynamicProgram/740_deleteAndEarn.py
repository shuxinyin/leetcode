class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = max(nums)
        A = [0] * (n + 1)
        for num in nums:
            A[num] += 1

        pre, cur = 0, A[1]
        for i in range(2, n + 1):
            pre, cur = cur, max(pre + A[i]*i, cur)
        return cur


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(nums[:-1])
