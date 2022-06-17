class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not \
                    0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True
            board[i][j] = ''  # 用过的原地修改，置空
            res = dfs(i + 1, j, k + 1) \
                  or dfs(i - 1, j, k + 1) \
                  or dfs(i, j + 1, k + 1) \
                  or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]  # 恢复原字母， 回溯
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


class Solution2:
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
                    if self.backtrack(i, j, mark, board, word[1:]):
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

            if 0 <= cur_i < len(board) \
                    and 0 <= cur_j < len(board[0]) \
                    and board[cur_i][cur_j] == word[0]:
                # 如果是已经使用过的元素，忽略
                if mark[cur_i][cur_j] == 1:
                    continue
                # 将该元素标记为已使用
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]):
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
        return False


