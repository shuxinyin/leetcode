class DoubleDividedPattern:
    @staticmethod
    def pattern(target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return l  # l永远是大于target的下一个数


# 剑指offer-11
class Solution:
    def minArray(self, numbers: [int]) -> int:
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            mid = l + (r - l) // 2

            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid  #
            else:
                r -= 1
        return numbers[l]


if __name__ == '__main__':
    nums = [7, 0, 1, 1, 1, 1, 1, 2, 3, 4]
    S =Solution()
    print(S.minArray(nums))