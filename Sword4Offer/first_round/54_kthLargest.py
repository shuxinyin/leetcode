# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            # 搜索树：节点值的大小：左中右（符合中序遍历）
            # search 第K大的节点值（则符合中序倒序遍历  右中左）
            if not root:
                return
            dfs(root.right)

            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res
