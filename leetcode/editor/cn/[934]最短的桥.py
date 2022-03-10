# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。） 
# 
#  现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。 
# 
#  返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。） 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：A = [[0,1],[1,0]]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：A = [[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length == A[0].length <= 100 
#  A[i][j] == 0 或 A[i][j] == 1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 232 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections

# 时间复杂度：O(MN)，其中M和N分别是数组A的行数和列数。
# 空间复杂度：O(MN)。
'''
通过对数组 A 中的 1 进行深度优先搜索，可以得到两座岛的位置集合，
分别为 source 和 target。
随后我们从 source 中的所有位置开始进行广度优先搜索，
当它们到达了 target 中的任意一个位置时，搜索的层数就是答案。
'''


class Solution(object):
    def shortestBridge(self, A):
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        print(source, target)
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d - 1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d + 1))
                    done.add(nei)


# leetcode submit region end(Prohibit modification and deletion)
class Solution2:
    # easy understand
    def shortestBridge(self, grid):
        from collections import deque
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        n = len(grid)
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

        while ql:
            i, j = ql.popleft()
            for d in dir:
                x, y = i + d[0], j + d[1]
                if 0 <= x < n and 0 <= y < n and grid[x][y]:
                    ql.append((x, y))
                    q.append((x, y))
                    grid[x][y] = 0

        step = 0
        vis = set(list(q))
        while q:
            w = len(q)
            for k in range(w):
                i, j = q.popleft()
                for d in dir:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < n and 0 <= y < n and (x, y) not in vis:
                        if grid[x][y]:
                            return step
                        q.append((x, y))
                        vis.add((x, y))
            step += 1


if __name__ == '__main__':
    A = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    res = 2
    S = Solution()
    print(S.shortestBridge(A))
