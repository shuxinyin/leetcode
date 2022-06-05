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
        # Time = O(N), 二叉搜索树的层数最小为logN（满二叉树），最大为N（退化为链表）。
        # Space = O(1)
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                break
        return root

    def lowestCommonAncestor_optimize(self, root, p, q) -> 'TreeNode':
        # 在第一步就比较p,q节点大小, 减少比较次数
        if p.val > q.val: p, q = q, p  # 保证 p.val < q.val
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                break
        return root

    def lowestCommonAncestor_recur(self, root, p, q) -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
