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

if __name__ == '__main__':
    NQueens = Solution_Queen()
    print(NQueens.n_queens2(4))