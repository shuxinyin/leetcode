class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        length = len(nums)
        positive, negative = int(nums[0] > 0), int(nums[0] < 0)
        maxLength = positive

        for i in range(1, length):
            if nums[i] > 0:
                positive += 1
                negative = (negative + 1 if negative > 0 else 0)
            elif nums[i] < 0:
                newPositive = (negative + 1 if negative > 0 else 0)
                newNegative = positive + 1
                positive, negative = newPositive, newNegative
            else:
                positive = negative = 0
            maxLength = max(maxLength, positive)
        return maxLength