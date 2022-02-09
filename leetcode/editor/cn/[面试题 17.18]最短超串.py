# 假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。 
# 
#  返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。 
# 
#  示例 1: 
# 
#  输入:
# big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
# small = [1,5,9]
# 输出: [7,10] 
# 
#  示例 2: 
# 
#  输入:
# big = [1,2,3]
# small = [4]
# 输出: [] 
# 
#  提示： 
# 
#  
#  big.length <= 100000 
#  1 <= small.length <= 100000 
#  
#  Related Topics 数组 哈希表 滑动窗口 👍 43 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestSeq(self, big, small):
        import collections
        minl, minr = -1, -1
        l, r = 0, 0
        min_len = len(big)
        need = collections.Counter(small)
        diff = len(small)

        while r < len(big):
            if big[r] in need:
                need[big[r]] -= 1
                if need[big[r]] >= 0:
                    diff -= 1

            while diff == 0:
                if r - l < min_len:
                    min_len = r - l
                    minl, minr = l, r

                if big[l] in need:  # 移动左边
                    need[big[l]] += 1
                    if need[big[l]] > 0:
                        diff += 1
                l += 1
            r += 1

        if minl == -1:
            return []
        return [minl, minr]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    big = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    small = [1, 5, 9]
    S = Solution()
    print(S.shortestSeq(big, small))
