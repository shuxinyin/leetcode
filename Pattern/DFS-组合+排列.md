## DFS-深度优先搜索

剑指 Offer 38. 字符串的排列
39-组合总和
40-组合总和II

78-子集
78-子集II

46.全排列
47.全排列II


#### 剑指 Offer 38. 字符串的排列
Q: 输入一个字符串，打印出该字符串中字符的所有排列。 里面不能有重复元素。

> 输入： 'abc'
> 输出： ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'] 


```python
class Solution:
    def permutation(self, s: str) -> List[str]:

        nums = list(s)
        if not nums:
            return 
        
        res = []
        nums.sort()
        n = len(nums)
        visited = [0] * n

        def dfs(tmp_list, length):
            if length == n:  # 出口
                res.append(''.join(tmp_list))
                return 

            # 重排（不再选自己）,用visited控制
            for i in range(n):
                # 访问过 或 （不是第一个数 & 不重复 & 上一个访问（因为有重复））
                if visited[i] or (i>0 and nums[i]==nums[i-1] and not visited[i-1]):
                    continue

                tmp_list.append(nums[i])
                visited[i] = 1
                dfs(tmp_list, len(tmp_list))
                visited[i] = 0

        helper([], 0)
        return res
```

#### 39-组合总和

Q:  给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target的所有 不同组合 ，并以列表形式返回。
你可以按 任意顺序 返回这些组合。 candidates 中的 同一个 数字可以 无限制重复被选取。 如果至少一个数字的被选数量不同，则两种组合是不同的。 

> 输入：candidates = [2,3,6,7], target = 7
> 输出：[[2,2,3],[7]]


```python
    def combinationSum(self, candidates, target):
        ''' 1. 可重复选自己
        '''
        res = []
        def dfs(begin, size, path, target):
            if target <0:
                return
            
            if target==0:
                res.append(path)
                return 

            # 重排（可再选自己）
            for i in range(begin, size):
                dfs(i, size, path + [candidates[i]], target-candidates[i])
        
        size = len(candidates)
        if size = 0:
            return res
        path = []
        dfs(candidates, 0, size, path, target)
        return res

```
#### 40-组合总和II

类似 剑指 Offer 38. 字符串的排列

Q: 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
    candidates 中的每个数字在每个组合中只能使用 一次 。 
    注意：解集不能包含重复的组合。 

> 输入: candidates =[10,1,2,7,6,1,5], target=8,
> 输出: [[1,1,6],[1,2,5],[1,7],[2,6]]

> 输入: candidates =[2,5,2,1,2], target =5,
> 输出: [[1,2,2],[5]]

```python
class Solution:
    def combinationSum2(self, candidates, target):
        ''' 1. 不重复选自己
            2.避免在同一层中使用相同的元素: 同等大小的数字下，如[2，2，2]，执行的是第一个2
        '''
        res = []
        def dfs(cand, path, target):
            if targe < 0:
                return 
            
            if target == 0:
                res.append(path)
                return 

            n = len(cand)
            for i in range(n):  # 排序完之后避免在同一层中使用相同的元素
                # tar小于下一个数或(i不是第一个数且前后数相等)时，跳过不执行搜索句，其他条件都执行
                if target>=cand[i] and not (i > 0 and cand[i] == cand[i-1]):
                    dfs(cand[i+1:], path + [candidates[i]], target-candidates[i])
        
        candidates.sort()
        path = []
        dfs(candidates, path, target)
```

#### 78-子集
Q: 给你一个整数数组 nums ，**数组中的元素 互不相同** 。返回该数组所有可能的子集（幂集）。 
    解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。 

> 输入：nums = [1,2,3]
> 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

```python
class Solution:
    def subsets(self, nums):
        '''1. 不重复选自己
        '''
        res = []

        n=len(nums)
        def dfs(part_nums, path):
            res.append(path)
            
            length = len(part_nums)
            for i in range(length):
                dfs(nums[i+1:], path+[part_nums[i]])
        
        path = []
        dfs(nums, path)
        return res

    def subsets2(self, nums):
        res = []
        n = len(nums)

        def dfs(i, n, tmp):
            res.append(tmp)
            for j in range(i, n):
                dfs(j + 1, n, tmp + [nums[j]])

        helper(0, n, [])
        return res
```

#### 78-子集II
Q:  给你一个整数数组 nums ，其中**可能包含重复元素**，请你返回该数组所有可能的子集（幂集）。 
    解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

>  输入：nums = [1,2,2]
>  输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        '''1. 不重复选自己
            2. 避免在同一层中使用相同的元素
        '''
        
        res = []
        def dfs(i, n, path):
            res.append(path)

            for j in range(i, n):
                # 终止出口在这里 i==n
                if j > i and nums[j] == nums[j-1]:
                    continue
                dfs(j+1, n, path + [nums[j]])
        
        dfs(0, n, [])
        return res
```


#### 46.全排列
Q: 给定一个**不含重复数字**的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 

> 输入：nums = [1,2,3]
> 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```python
class Solution(object):
    def permute(self, nums):
        ''' 1. 不重复选自己
        '''
        res = []
        def dfs(start, size, path):
            if len(path) == size:
                res.append(path)

            for j in range(start, size):
                dfs(j+1, size, path + [nums[j]])
        
        path = []
        dfs(0, len(nums), path)
        return res

```

#### 46.全排列II
Q:  给定一个可**包含重复数字**的序列 nums ，按任意顺序 返回所有不重复的全排列。 

> 输入：nums = [1,1,2]
> 输出：[[1,1,2], [1,2,1], [2,1,1]]

```python
class Solution():
    def permuteUnique(self, nums):
        '''1. 不重复选自己
            2. 同层间不选相同的数字
        '''
        res = []
        nums.sort()
        def dfs(start, size, path):
            if len(path) == size:
                res.append(path)

            for i in range(start, size):
                if i>0  and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, size, path+[nums[i]])
        
        path = []
        dfs(0, len(nums), path)
        return res

    def permuteUnique2(self, nums):
        if not nums:
            return

        res = []
        nums.sort()
        n = len(nums)
        visited = [0] * n

        def helper1(temp_list, length):
            if length == n:
                res.append(temp_list)
            for i in range(n):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = 1
                helper1(temp_list + [nums[i]], length + 1)
                visited[i] = 0

        helper1([], 0)
        return res

```


### 总结：
关于这类问题，有这么几点需要注意：
1. 是否可以重复选自己
2. 数组中是否含有相同数字

关于问题1-不重复选自己，dfs两种写法
```python

def dfs(part_nums, path):
    # 控制 nums 数组
    if len(path) <= len(n):
        res.append(path)
        return 
    
    length = len(part_nums)
    for i in range(length):
        dfs(nums[i+1:], path+[part_nums[i]])

def dfs(start, size, path):
    # 控制 index
    if len(path) <= len(n):
        res.append(path)
        return 
    
    for j in range(i， size):
        dfs(j+1, size, path+[nums[j]])
```

关于问题2-避免 同一层 选相同的数字，dfs写法

```python

nums.sort()
def dfs(i, n, path):
    res.append(path)

    for j in range(i, n):
        # 终止出口在这里 i==n
        if j > i and nums[j] == nums[j-1]:
            continue
        dfs(j+1, n, path + [nums[j]])
```