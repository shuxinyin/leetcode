# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，
# 并将这些区域里所有的 'O' 用 'X' 填充
# 。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O",
# "X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
# 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["X"]]
# 输出：[["X"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] 为 'X' 或 'O' 
#  
#  
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 741 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve_DFS(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS  Time:O(M*N) Space:O(M*N)
        if not board:
            return
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(board), len(board[0])

        def dfs(x, y):
            # search 墙边='O' 与 墙边连着='O'的位置，都使='B'
            board[x][y] = "B"
            for direc in directions:
                cur_x = x + direc[0]
                cur_y = y + direc[1]
                if 0 <= x < row or 0 <= y < col or board[x][y] == "O":
                    dfs(cur_x, cur_y)

        # 遍历围墙的四条边
        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                dfs(row - 1, j)
        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][col - 1] == "O":
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"

    def solve_BFS(self, board):
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def bfs(i, j):
            # search 墙边='O' 与 墙边连着='O'的位置，都使='B'
            from collections import deque
            queue = deque()
            queue.appendleft((i, j))
            while queue:
                i, j = queue.pop()
                if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
                    board[i][j] = "B"
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.appendleft((i + x, j + y))

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                bfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                bfs(row - 1, j)

        for i in range(row):

            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col - 1] == "O":
                bfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    out = [["X", "X", "X", "X"],
           ["X", "X", "X", "X"],
           ["X", "X", "X", "X"],
           ["X", "O", "X", "X"]]
