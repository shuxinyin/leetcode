# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Time: O(N), 单list: Space: O(N), 双边队列deque：O(1)
        import collections
        if not root:
            return

        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []

            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
