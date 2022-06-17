# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return str(root.val) + ',' \
               + self.Serialize(root.left) + ',' \
               + self.Serialize(root.right)

    def deserialize(self, s):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        list = s.split(',')
        return self.DeserializeTree(list)

    def DeserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.DeserializeTree(list)
            root.right = self.DeserializeTree(list)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
