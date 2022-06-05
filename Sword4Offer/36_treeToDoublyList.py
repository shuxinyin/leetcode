"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            # 中序遍历
            if not cur:
                return
            dfs(cur.left)

            if self.pre:  # 修改节点引用 -双向
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 移动pre节点

            dfs(cur.right)

        if not root:
            return
        self.pre =None
        dfs(root)
        #  节点循环修改
        self.head.left, self.pre.right = self.pre, self.head
        return self.head