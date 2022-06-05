# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # Time: O(M*N), Space: O(M)  M,N分别为树A和树B的节点数量

        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False

            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and \
               (recur(A, B) or self.isSubStructure(A.left, B) or \
                self.isSubStructure(A.right, B))
