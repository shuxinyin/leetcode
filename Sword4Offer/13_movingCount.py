class Solution:
    def digitsum(self, n):
        ans = 0
        while n:
            ans += n % 10
            n //= 10
        return ans

    def movingCount(self, m: int, n: int, k: int) -> int:
        # Time: O(mn), 格子数目
        # Space: O(mn), set中含有的最大格子数目，二维坐标
        # 只需要向左向下扫描

        from queue import Queue
        q = Queue()
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
