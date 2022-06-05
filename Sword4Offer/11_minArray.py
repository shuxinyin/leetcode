class Solution:
    def minArray(self, numbers: [int]) -> int:
        # Time: O(log(N)), Space: O(1)
        n = len(numbers)

        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r -= 1
        return numbers[l]


if __name__ == '__main__':
    l = [1, 3, 5]
    S = Solution()
    print(S.minArray(l))
