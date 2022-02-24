# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用 一次 。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates =[10,1,2,7,6,1,5], target=8,
# 输出: [[1,1,6],[1,2,5],[1,7],[2,6]]
# 
#  示例 2: 
# 
#  
# 输入: candidates =[2,5,2,1,2], target =5,
# 输出: [[1,2,2],[5]]
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
#  Related Topics 数组 回溯 👍 845 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates, target):
        def dfs(cand, tar, path, res):
            if tar < 0:
                return
            if tar == 0:
                res.append(path)
                return
            n = len(cand)
            for i in range(n):  # 排序完之后避免在同一层中使用相同的元素
                # tar小于下一个数或(i不是第一个数且前后数相等)时，跳过不执行搜索句，其他条件都执行
                # 这里保证的是在同等大小的数字下，如【2，2，2】，执行的是第一个2
                if target >= cand[i] and not (i > 0 and cand[i] == cand[i - 1]):
                    # candidates[i+1:]从第i+1个数开始搜索
                    dfs(cand[i + 1:], tar - cand[i], path + [cand[i]], res)

        candidates.sort()  # 先排序（因为需要比较前后一个值是否相同）
        res, path = [], []
        dfs(candidates, target, path, res)
        return res
# leetcode submit region end(Prohibit modification and deletion)
