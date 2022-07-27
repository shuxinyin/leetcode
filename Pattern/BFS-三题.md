## BFS-广度优先搜索

126-单词接龙
127-单词接龙II
934-最短的桥

### 126-单词接龙
Q: # 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，
并满足： 每对相邻的单词之间仅有单个字母不同。 转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。 
**输出最短序列的长度**。

> 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot", "log","cog"]  
> 输出：5  
> 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。  


```python
from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        ''' BFS + 双边队列deque
        1. 取deque存最短序列， visited进行标记已访问
        2. while deque:
                word=deque.popleft(), 
                for j in range(word_len):  # 遍历word字符
                    for k in range(26):  # 遍历26个字母
                        # 将word逐个替换，得到next_word
                        if next_word in wordList: 判断是否存在给的单词list中
                    恢复原word, 继续进行上述操作
        '''
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()

                word_list = list(word)
                for j in range(word_len):
                    # 先保存，最后恢复
                    origin_char = word_list[j]
                    
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                # 注意：添加到队列以后，必须马上标记为已经访问
                                visited.add(next_word)
                    word_list[j] = origin_char  # 恢复
            step += 1
        return 0

```

### 127-单词接龙II

Q:  按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，
并满足： 每对相邻的单词之间仅有单个字母不同。 转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。 
输出最短序列的list集合。

> 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
> "log","cog"]
> 输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
> 解释：存在 2 种最短的转换序列：
> "hit" -> "hot" -> "dot" -> "dog" -> "cog"
> "hit" -> "hot" -> "lot" -> "log" -> "cog"

```python

import string
from collections import deque, defaultdict

class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res

        successors = defaultdict(set)
        # 第 1 步：使用广度优先遍历得到后继结点列表 successors

        found = self.__bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res
        # 第 2 步：基于后继结点列表 successors ，使用回溯算法得到所有最短路径列表
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res

    def __bfs(self, beginWord, endWord, word_set, successors):
        ''' successors: key：字符串，value：广度优先遍历过程中 key 的后继结点列表
        '''
        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        found = False
        word_len = len(beginWord)
        next_level_visited = set()

        while queue:
        # 与126 bfs一致， 查找可接龙的下一个字符串
            current_size = len(queue)
            for i in range(current_size):
                current_word = queue.popleft()
                word_list = list(current_word)

                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)

                        if next_word in word_set:
                            if next_word not in visited:
                                if next_word == endWord:
                                    found = True

                                # 避免下层元素重复加入队列
                                if next_word not in next_level_visited:
                                    next_level_visited.add(next_word)
                                    queue.append(next_word)

                                successors[current_word].add(next_word)
                    word_list[j] = origin_char
            if found:
                break
            # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
            visited |= next_level_visited
            next_level_visited.clear()
        return found

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_words = successors[beginWord]
        for next_word in successor_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()

```

### 934-[最短的桥](https://leetcode.cn/problems/shortest-bridge/)

Q:  在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）

> ```
> 输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
> 输出：1
> ```

```python
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        from collections import deque
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        n = len(grid[0])
        q = deque()
        ql = deque()
        i = 0
        # 找到第一个=1的位置
        while not q:
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    ql.append((i, j))
                    grid[i][j] = 0
                    break
            i += 1

        # 由第一个=1的位置，进行BFS, 找到所有的邻近的=1的点, 存进q同时置为0，表示第一个岛
        while ql:
            i, j = ql.popleft()
            for d in dir:
                x, y = i + d[0], j + d[1]
                if 0 <= x < n and 0 <= y < n and grid[x][y]:
                    ql.append((x, y))
                    q.append((x, y))
                    grid[x][y] = 0

        # 从岛屿q出发, BFS, 查找还剩余=1的位置，此时step数即为深度
        step = 0
        vis = set(list(q))
        while q:
            w = len(q)
            for k in range(w):  # 遍历原岛屿q的每一个位置进行BFS搜索
                i, j = q.popleft()
                for d in dir:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < n and 0 <= y < n and (x, y) not in vis:
                        if grid[x][y]:
                            return step
                        q.append((x, y))  # 下一层，继续重复上述进行搜索
                        vis.add((x, y))
            step += 1
```



