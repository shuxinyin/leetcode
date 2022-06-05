# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Time = O(N), N为节点数量
        # Space = O(N), N为节点数量
        def recur(root):
            if not root:
                return 0

            l = recur(root.left)
            if l == -1:
                return -1

            r = recur(root.right)
            if r == -1:
                return -1

            return max(l, r) + 1 if abs(l - r) <= 1 else -1

        return recur(root) != -1


class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        # Time = 每层执行复杂度 × 层数复杂度 = O(N×logN)
        # Space = O(N)
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 \
               and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
