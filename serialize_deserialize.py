#coding=utf-8
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    297. Serialize and Deserialize Binary Tree

    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def _serialize(root):
            if not root:
                return vals.append('#')
            vals.append(str(root.val))
            _serialize(root.left)
            _serialize(root.right)
        _serialize(root)
        return ' '.join(vals)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        node_list = data.split(' ')
        def _deserialize(node_list):
            root_val = node_list.popleft()
            if root_val != '#':
                root = TreeNode(int(root_val))
                root.left = _deserialize(node_list)
                root.right = _deserialize(node_list)
            else:
                return None
            return root
        return _deserialize(deque(node_list))

