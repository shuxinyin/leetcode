### DFS-回溯

79.单词搜索
695.岛屿的最大面积
547.省份数量
417.太平洋大西洋水流问题

51.N皇后
52.N皇后II

679.24点游戏

#### 79.单词搜索

> Q: 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
> 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

> 示例 1：
> 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
> 输出：true

```python
class Solution:
    # 定义上下左右四个行走方向
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # 将该元素标记为已使用
                    mark[i][j] = 1
                    if self.backtrack(i, j, mark, board, word[1:]) == True:
                        return True
                    else:
                        # 回溯
                        mark[i][j] = 0
        return False

    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True

        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]

            if 0 <= cur_i < len(board) and 0 <= cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                # 如果是已经使用过的元素，忽略
                if mark[cur_i][cur_j] == 1:
                    continue
                # 将该元素标记为已使用
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
        return False
```

#### 695.岛屿的最大面积

> 给你一个大小为 m x n 的二进制矩阵 grid 。
> 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设
> grid 的四个边缘都
> 被 0（代表水）包围着。
> 岛屿的面积是岛上值为 1 的单元格的数目。 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
>
>  示例 1：
> 输入：grid = [
> [0,0,1,0,0,0,0,1,0,0,0,0,0],
> [0,0,0,0,0,0,0,1,1,1,0,0,0],
> [0,1,1,0,1,0,0,0,0,0,0,0,0],
> [0,1,0,0,1,1,0,0,1,0,1,0,0],
> [0,1,0,0,1,1,0,0,1,1,1,0,0],
> [0,0,0,0,0,0,0,0,0,0,1,0,0],
> [0,0,0,0,0,0,0,1,1,1,0,0,0],
> [0,0,0,0,0,0,0,1,1,0,0,0,0]]
> 输出：6
> 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。

```python
class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maxAreaOfIsland(self, grid):
        ans = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                ans = max(self.dfs(i, j, grid), ans)
        return ans

    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1:
            return 0

        grid[i][j] = 0  # 表示此地已用
        ans = 1
        for direc in self.directs:
            cur_i = i + direc[0]
            cur_j = j + direc[1]

            ans += self.dfs(cur_i, cur_j, grid)
        return ans
```

#### 547.省份数量

> 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市
> c 间接相连。
> 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
>
>  给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j
> 个城市直接相连，而isConnected[i][j] = 0 表示二者不直接相连。
> 返回矩阵中 省份 的数量。
>
> 示例 1：
> 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
> 输出：2

```python
class Solution:
    def findCircleNum(self, isConnected):
        print()


```

#### 417.太平洋大西洋水流问题

> 有一个 m × n 的长方形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。
> 这个岛被分割成一个个方格网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度
> 。
>
>  岛上雨水较多，如果相邻小区的高度 小于或等于 当前小区的高度，雨水可以直接向北、南、东、西流向相邻小区。水可以从海洋附近的任何细胞流入海洋。
> 返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格 (ri, ci) 流向 太平洋和大西洋。
>
>  示例 1：
>
> 输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
> 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

```python
class Solution:
    def pacificAtlantic(self, matrix):
        pass


```

#### 51.N皇后

> n 皇后问题：在一个 n * n 的棋盘上放置 n 个皇后，要求不能有两个皇后位于同一行、同一列，或同一条 45 度斜线上。
> 1.还有一种问题是输出每一种放法？（51.N皇后 即输出一个放法矩阵） 2.问共有多少种放法？(52.N皇后II)

> 解析：假设现在已在棋盘放下的位置为(i, pos[i])，下一个试探落位的为(row, col), 则需检查以下三点（列，撇，捺是否冲突）：
> 1. 同一列： col = pos[i]
> 2. 同一撇： col - pos[i] = row - i
> 3. 同一捺： col - pos[i] = i - row

```python
class Solution:
    def n_queens_method1(self, n):



```

#### 52.N皇后II

#### 679.24点游戏

> 给定一个长度为4的整数数组 cards 。你有 4 张卡片，每张卡片上都包含一个范围在 [1,9] 的数字。
> 您应该使用运算符 ['+', '-', '*', '/'] 和括号 '(' 和 ')' 将这些卡片上的数字排列成数学表达式，以获得值24。
> 你须遵守以下规则:
> 除法运算符 '/' 表示实数除法，而不是整数除法。
> 例如， 4 /(1 - 2 / 3)= 4 /(1 / 3)= 12 。
> 每个运算都在两个数字之间。特别是，不能使用 “-” 作为一元运算符。
> 例如，如果 cards =[1,1,1,1] ，则表达式 “-1 -1 -1 -1” 是 不允许 的。
> 你不能把数字串在一起
> 例如，如果 cards =[1,2,1,2] ，则表达式 “12 + 12” 无效。
> 如果可以得到这样的表达式，其计算结果为 24 ，则返回 true ，否则返回 false 。
> 示例 1:
> 输入: cards = [4, 1, 8, 7]
> 输出: true
> 解释: (8-4) * (7-1) = 24

```python
class Solution:
    def __init__(self):
        self.add = 0
        self.multiply = 1
        self.subtract = 2
        self.divide = 3
        self.target = 24
        self.epsilon = 1e-6  # 除法运算为实数除法，因此结果为浮点数，列表中存储的数字也都是浮点数。在判断结果是否等于 2424 时应考虑精度误差，这道题中，误差小于 10−610−6 可以认为是相等


    def judgePoint24(self, cards: [int]) -> bool:

        return self.dfs(cards)

    def dfs(self, nums):
        if not nums:
            return False
        if len(nums) == 1:
            return abs(nums[0] - self.target) < self.epsilon

        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                new_nums = []

                for k in range(n):
                    if k != i and k != j:
                        new_nums.append(nums[k])

                a, b = nums[i], nums[j]

                for v in range(4):
                    # 加法和乘法都满足交换律，因此如果选择的运算操作是加法或乘法，则对于选出的2
                    # 个数字不需要考虑不同的顺序，在遇到第二种顺序时可以不进行运算，直接跳过。
                    if v < 2 and i > j:
                        continue
                    if v == self.add:
                        new_nums.append(a + b)
                    if v == self.multiply:
                        new_nums.append(a * b)
                    if v == self.subtract:
                        new_nums.append(a - b)
                    if v == self.divide:
                        if abs(b) < self.epsilon:
                            continue
                        new_nums.append(a / b)

                    if self.dfs(new_nums):
                        return True
                    new_nums.pop()
        return False
```