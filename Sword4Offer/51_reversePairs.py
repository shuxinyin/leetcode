class Solution:
    def merge(self, left_nums, right_nums):
        res = []
        i, j = 0, 0
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] <= right_nums[j]:
                res.append(left_nums[i])
                i += 1
            else:
                res.append(right_nums[j])
                self.count += len(left_nums) - i
                j += 1

        if i == len(left_nums):
            res += right_nums[j:]
        else:
            res += left_nums[i:]
        return res

    def merge_sort(self, nums):
        length = len(nums)
        if length <= 1:
            return nums

        mid = length // 2
        left_nums = self.merge_sort(nums[:mid])
        right_nums = self.merge_sort(nums[mid:])

        return self.merge(left_nums, right_nums)

    def reversePairs(self, nums: [int]) -> int:
        self.count = 0
        self.merge_sort(nums)
        return self.count


if __name__ == '__main__':
    nums = [7, 3, 2, 6, 0, 1, 5, 4]
    S = Solution()
    # print(S.reversePairs(nums))
    print(S.reversePairs([]))
