# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# 输出: 4
# 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# 输出: 10
#  
# 
#  
# 
#  提示: 
# 
#  
#  m == heightMap.length 
#  n == heightMap[i].length 
#  1 <= m, n <= 200 
#  0 <= heightMap[i][j] <= 2 * 10⁴ 
#  
# 
#  
#  Related Topics 广度优先搜索 数组 矩阵 堆（优先队列） 👍 622 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trapRainWater(self, heightMap: [[int]]) -> int:
        ''' 优先队列 + DFS
            队列存最外层元素, 保持pop最小v(小顶堆)
             创建visited(表示是否已经灌水过)  DFS搜索v邻居点，进行灌水
        '''
        import heapq
        r, c = len(heightMap), len(heightMap[0])
        visited = [[0 for _ in range(c)] for _ in range(r)]

        pq = []
        for i in range(r):
            for j in range(c):
                if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        print(len(pq), pq)

        res = 0
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while pq:
            h, x, y = heapq.heappop(pq)
            for (i, j) in dirs:
                cur_x, cur_y = x + i, y + j

                if 0 <= cur_x and cur_x < r and 0 <= cur_y and cur_y < c and visited[cur_x][cur_y] == 0:
                    tmp = h - heightMap[cur_x][cur_y]
                    if tmp > 0:
                        # print(heightMap[cur_x][cur_y], cur_x, cur_y)
                        res += tmp
                    visited[cur_x][cur_y] = 1
                    heapq.heappush(pq, (max(h, heightMap[cur_x][cur_y]), cur_x, cur_y))
        return res

# class Solution:
#     def trapRainWater(self, heightMap: [[int]]) -> int:
#         import heapq
#
#         if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
#             return 0
#
#         m, n = len(heightMap), len(heightMap[0])
#         visited = [[0 for _ in range(n)] for _ in range(m)]
#         pq = []
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 or i == m - 1 or j == 0 or j == n - 1:
#                     visited[i][j] = 1
#                     heapq.heappush(pq, (heightMap[i][j], i * n + j))
#
#         res = 0
#         dirs = [-1, 0, 1, 0, -1]
#         while pq:
#             height, position = heapq.heappop(pq)
#             for k in range(4):
#                 nx, ny = position // n + dirs[k], position % n + dirs[k + 1]
#                 if nx >= 0 and nx < m and ny >= 0 and ny < n and visited[nx][ny] == 0:
#                     if height > heightMap[nx][ny]:
#                         res += height - heightMap[nx][ny]
#                     visited[nx][ny] = 1
#                     heapq.heappush(pq, (max(height, heightMap[nx][ny]), nx * n + ny))
#         return res

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    heightMap = [[1, 4, 3, 1, 3, 2],
                 [3, 2, 1, 3, 2, 4],
                 [2, 3, 3, 2, 3, 1]]
    S = Solution()
    print(S.trapRainWater(heightMap))
