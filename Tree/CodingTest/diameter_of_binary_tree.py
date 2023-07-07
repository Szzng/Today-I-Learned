# https://leetcode.com/problems/diameter-of-binary-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def depth(self, node):
        if node is None: return 0

        left = self.depth(node.left)
        right = self.depth(node.right)

        self.diameter = max(left + right, self.diameter)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.diameter
