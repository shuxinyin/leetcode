# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 
# 
#  你可以按 任何顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, k = 1
# 输出：[[1]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
#  Related Topics 数组 回溯 👍 884 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n, k):
        res, track = [], []
        self.dfs(n, k, 1, track, res)

        return res

    def dfs(self, n, k, start, track, res):
        if len(track) == k:
            res.append(track[:])

        for i in range(start, n + 1):
            track.append(i)
            self.dfs(n, k, i + 1, track, res)
            track.pop()


class Solution1:
    def combine(self, n, k):
        result, track = [], []
        self.backtrack(n, k, 1, track, result)
        return result

    def backtrack(self, n, k, start, track, result):
        if len(track) == k:
            result.append(track[:])
        for i in range(start, n + 1):
            track.append(i)
            self.backtrack(n, k, i + 1, track, result)
            track.pop()


class Solution2:
    # dfs + 剪枝版
    def combine(self, n, k):
        result, track = [], []
        self.backtrack(n, k, 1, track, result)
        return result

    def backtrack(self, n, k, start, track, result):
        if k == 0:
            result.append(track[:])
            return
        for i in range(start, n - k + 2):
            track.append(i)
            self.backtrack(n, k - 1, i + 1, track, result)
            track.pop()


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n, k = 4, 2
    S = Solution()
    print(S.combine(n, k))

