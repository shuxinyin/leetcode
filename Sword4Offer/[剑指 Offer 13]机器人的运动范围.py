# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一
# 格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但
# 它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？ 
# 
#  
# 
#  示例 1： 
# 
#  输入：m = 2, n = 3, k = 1
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：m = 3, n = 1, k = 0
# 输出：1
#  
# 
#  提示： 
# 
#  
#  1 <= n,m <= 100 
#  0 <= k <= 20 
#  
#  Related Topics 深度优先搜索 广度优先搜索 动态规划 👍 525 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def digitsum(self, n):
        ans = 0
        while n:
            ans += n % 10
            n = n // 10
        return ans

    def movingCount(self, m: int, n: int, k: int) -> int:
        '''广度优先搜索
        '''
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        res = set()

        while not q.empty():
            x, y = q.get()
            if (x, y) not in res \
                    and x < m and y < n and self.digitsum(x) + self.digitsum(y) <= k:
                res.add((x, y))

                for nx, ny in [(x+1, y), (x, y+1)]:
                    q.put((nx, ny))

        return len(res)

class Solution:
    def digitsum(self, n):
        '''对 n 求数字和
        '''
        ans = 0
        while n:
            ans += n % 10
            n //= 10
        return ans

    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()  # 队列
        q.put((0, 0))
        s = set()

        while not q.empty():
            x, y = q.get()
            if (x, y) not in s \
                    and 0 <= x < m and 0 <= y < n \
                    and self.digitsum(x) + self.digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    from queue import Queue

    q = Queue()  # 栈
    q.put((0, 0))
    q.put((1, 1))

    while not q.empty():
        print(q.get())
