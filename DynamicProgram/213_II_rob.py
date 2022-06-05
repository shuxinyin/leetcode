class Solution:
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        # 将环转化为两个list（取头去尾[:-1], 取尾去头[1:]）, 取最大返回
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(nums[:-1])