#### 剑指 Offer 36. 二叉搜索树与双向链表
class Solution:
    def treeToDoublyList(self, root):
        ''' 二叉搜索树 转换成 排序双向链表
            left < root < right
        '''

        # 中序遍历
        def dfs(cur):
            if not root:
                return
            dfs(root.left)

            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(root.right)

        if not root:
            return
        self.pre = None
        dfs(root)
        self.pre.right, self.head.left = self.head, self.pre
        return self.head


class Solution_Queen:
    def n_queens1(self, n):
        '''NQueens 暴力法
        pos[i] = j, 表示（i，j）有一个皇后，
        现在第 i 行已经有一个皇后放置在 (i, pos[i])， 判断是否能放下一个皇后（row, col），需检测三个维度
            1.同一列： col = pos[i]
            2.同一撇： col - pos[i] = row - pos[i]
            3.同一捺： col - pos[i] = pos[i] - row
        '''
        count = 0
        pos = [0] * n

        def check(i, j):
            pass

        def dfs(row):
            for col in range(n):
                # 检查冲突
                ok = True
                for i in range(row):
                    if col == pos[i] or col - pos[i] == row - i or col - pos[i] == i - row:
                        ok = False
                        break
                if not ok:
                    continue

    def n_queens2(self, n):
        pos = [0] * n  # 已放置的皇后的列号
        self.count = 0  # 解法总数

        def DFS(row):  # 递归函数，试探第 row 行皇后的位置
            # global count
            for col in range(n):  # 依次试探每一列
                # 检查冲突
                ok = True
                for i in range(row):
                    if col == pos[i] or col - pos[i] == row - i or col - pos[i] == i - row:
                        ok = False
                        break
                if not ok:
                    continue
                # 检查冲突结束
                if row == n - 1:  # 已放到最后一行
                    print(row, col, pos)
                    self.count += 1  # 找到一组解
                else:
                    # print(row, col, pos)
                    pos[row] = col  # 记录当前行皇后的位置
                    DFS(row + 1)
                    # pos[row] = 0  # 因为sol[row]在下一次被写之前不会被读，不要还原

        DFS(0)
        return self.count


class SortSolution:
    def quick_sort(self, nums, l, r):

        if l >= r:
            return nums
        i, j = l, r
        pivot = nums[l]

        while i < j:
            while i < j and nums[i] <= pivot:
                i += 1
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[l], nums[i] = nums[i], nums[l]  # 把标杆插到中间，左边都是 < pivot, 右边都是 > pivot
        self.quick_sort(nums, l, i - 1)
        self.quick_sort(nums, i + 1, r)
        return nums

    def merge(self, left_nums, right_nums):
        res = []
        i, j = 0, 0
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] < right_nums[j]:
                res.append(left_nums[i])
                i += 1
            else:
                res.append(right_nums[j])
                j += 1

        if i == len(left_nums):
            res += right_nums[j:]
        else:
            res += left_nums[i:]
        return res

    def merge_sort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums

        l, r = 0, n
        mid = l + (r - l) // 2

        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def heapify(self, nums, n, i):
        """构建大顶堆： 构建以i为root的最大堆"""
        if i >= n:
            return
        l = 2 * i + 1
        r = 2 * i + 2
        max_ind = i  # 最大值的下标

        if l < n and nums[l] > nums[max_ind]:
            max_ind = l
        if r < n and nums[r] > nums[max_ind]:
            max_ind = r

        if max_ind != i:  # 把最大值放到i上,即根节点, 建最大堆
            nums[i], nums[max_ind] = nums[max_ind], nums[i]
            self.heapify(nums, n, max_ind)

    def build_heap(self, nums, n):
        ''' 建堆，使得nums满足堆的要求
            自下而上：从最后一个节点的parent(最后一个非叶子节点)开始
        '''
        last_node = n - 1
        parent = (last_node - 1) // 2
        for i in range(parent, -1, -1):
            self.heapify(nums, n, i)

    def heap_sort(self, nums, n):
        ''' 包含两步：1.建堆， 使得nums满足堆的要求
                    2. 排序， 将堆顶元素，放置队尾，砍断，继续建堆
        '''
        self.build_heap(nums, n)
        for i in range(n - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)  # i为列队 数量, 一直减少表示砍断顶点（最大值），所以最后输出升序


class BackPack:
    # 背包三讲
    def bp01(self, capacity, weights, values):
        N = len(weights)

        dp = [0] * (capacity + 1)
        for i in range(1, N + 1):
            w, v = weights[i - 1], values[i - 1]
            for j in range(capacity, w - 1, -1):
                dp[j] = max(dp[j - 1], dp[j - w] + v)

        return dp[-1]

    def bp_complete(self, capacity, weights, values):
        N = len(weights)

        dp = [0] * (capacity + 1)
        for i in range(1, N + 1):
            w, v = weights[i - 1], values[i - 1]
            for j in range(w, capacity):
                dp[j] = max(dp[j - 1], dp[j - w] + v)

        return dp[-1]

    def coinChange(self, coins: [int], amount: int) -> float:
        # Q: 给你一个整数数组
        # coins ，表示不同面额的硬币；以及一个整数
        # amount ，表示总金额。 计算可以凑成总金额所需的
        # 最少的硬币个数

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        n = len(coins)
        for i in range(n):
            w = coins[i]
            for j in range(w, amount + 1):
                dp[j] = min(dp[j - 1], dp[j - w] + 1)
        return dp[-1]

    def numSquares(self, n: int):
        dp = [float("inf")] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = i
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]

    def integerBreak(self, n: int):
        # Q: 给定一个正整数n ，将其拆分为k个正整数的和（ k >= 2 ），并使这些整数的乘积最大化。
        # dp[i]表示 和 为 i 的k个正整数的最大乘积
        # 转移： dp[i] = max(dp[i-1], dp[i-j]*j)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = i
            j = 1
            while j < i:
                dp[i] = max(dp[i - 1], dp[i - j] * j)
                j += 1
            return dp[-1]

    def change(self, amount: int, coins: [int]):
        n = len(coins)

        dp = [0] * (amount + 1)



if __name__ == '__main__':
    # NQueens = Solution_Queen()
    S = SortSolution()
    # print(S.quick_sort([1, 2, 4, 5, 3]))
    # nums = [4, 10, 3, 5, 1, 2]
    nums = [2, 5, 3, 1, 10, 4]
    n = 6
    S.heap_sort(nums, 6)

    # S.heapify(nums, n, 0)
    print(nums)
