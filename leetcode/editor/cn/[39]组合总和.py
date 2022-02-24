# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的
#  所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。 
# 
#  candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
# 
#  对于给定的输入，保证和为 target 的不同组合数少于 150 个。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。 
# 
#  示例 2： 
# 
#  
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]] 
# 
#  示例 3： 
# 
#  
# 输入: candidates = [2], target = 1
# 输出: []
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= candidates.length <= 30 
#  1 <= candidates[i] <= 200 
#  candidate 中的每个元素都 互不相同 
#  1 <= target <= 500 
#  
#  Related Topics 数组 回溯 👍 1762 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum(self, candidates, target):
        '''
        Analyze:
        Func:
            判断target：
                等于0， res.append(path)
                小于0，返回上一层
                大于0：继续往下遍历
            从第一个元素i=0 in (0,len)开始搜索：
                path = path.append(cand[i])
                设置 target = target - cand[i],回溯调Func
                path.remove(cand[i])
        '''
        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                # path  =path + [candidates[index]] //思想
                # path[-1].pop() // （这一步实现需要更多的逻辑判断），直接融合到参数这体现更简洁
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8
    S = Solution()
    print(S.combinationSum(candidates, target))
