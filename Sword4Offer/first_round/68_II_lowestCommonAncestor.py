# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 三种情况: 1. p, q在root右侧
        #           2. p, q在root左侧
        #           3. p, q在root两侧,return root
        # 时间复杂度O(N)： 其中N为二叉树节点数；最差情况下，需要递归遍历树的所有节点。空间复杂度
        # Space O(N) ： 最差情况下，递归深度达到N ，系统使用O(N)大小的额外空间。

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root