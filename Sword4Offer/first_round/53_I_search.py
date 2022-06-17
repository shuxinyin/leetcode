import collections


class Solution:
    def search(self, nums, target: int) -> int:
        # dict method
        # Time: O(N), Space: O(N)
        dic = collections.defaultdict(int)

        for n in nums:
            dic[n] += 1
        return dic[target]

    def search2(self, nums, target: int) -> int:
        # double divide: 模板 attention
        # 1.search left margin  2.search right margin 3. return r-l
        # Time: O(logN), Space: O(1)
        def search_right_margin(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = i + (j - i) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i  # i永远是大于target的下一个数

        return search_right_margin(target) - search_right_margin(target - 1)



if __name__ == '__main__':
    l = [5, 7, 7, 8, 8, 10]
    l = [1]
    t = 1

    S = Solution()
    print(S.search3(l, t))
