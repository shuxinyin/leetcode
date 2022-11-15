# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。 
# 
#  假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
# 
#  
# 
#  示例 1: 
# 
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/ 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 865 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 前序列： 中左右， 中序：左中右
        index = {k: v for k, v in enumerate(inorder)}

        def build(pre_left, pre_right, in_left, in_right):
            inorder_root = index[preorder[pre_left]]
            sub_len = inorder_root - in_left

            root = TreeNode(preorder[pre_left])

            root.left = build(pre_left + 1, pre_left + sub_len, in_left, inorder_root - 1)
            root.right = build(pre_left + sub_len + 1, pre_right, inorder_root + 1, in_right)
            return root

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)
# leetcode submit region end(Prohibit modification and deletion)
