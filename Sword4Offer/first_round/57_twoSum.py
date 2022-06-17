class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        # Time: O(N), Space: O(N)

        dic = {}
        for n in nums:

            if n not in dic:
                dic[target - n] = n
            else:
                return [dic[n], n]
        return -1


if __name__ == '__main__':
    S = Solution()
    print(S.twoSum([2, 7, 11, 15], 9))
