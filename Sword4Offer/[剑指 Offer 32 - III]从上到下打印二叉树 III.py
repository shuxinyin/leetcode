# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。 
# 
#  
# 
#  例如: 
# 给定二叉树: [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 1000 
#  
#  Related Topics 树 广度优先搜索 二叉树 👍 233 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def levelOrder(self, root: TreeNode) -> List[List[int]]:
            # Time: O(N), 单list: Space: O(N)
            import collections
            if not root:
                return []

            res, deque = [], collections.deque([root])
            while deque:
                tmp = collections.deque()
                for _ in range(len(deque)):
                    node = deque.popleft()

                    if len(res) % 2:
                        tmp.appendleft(node.val)  # 偶数层 -> 队列头部
                    else:
                        tmp.append(node.val)  # 奇数层 -> 队列尾部

                    if node.left:
                        deque.append(node.left)
                    if node.right:
                        deque.append(node.right)
                res.append(list(tmp))
            return res

        def levelOrder2(self, root: TreeNode) -> List[List[int]]:
            # Time: O(N), 单list: Space: O(N)
            # 放最后， len(res)为奇数，说明当前层为偶数，进行倒叙，反之正序
            import collections
            if not root: return []
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
                res.append(tmp[::-1] if len(res) % 2 else tmp)
            return res
# leetcode submit region end(Prohibit modification and deletion)
