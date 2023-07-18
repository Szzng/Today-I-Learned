# https://leetcode.com/problems/subtree-of-another-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isSameNode(self, n1, n2):
        if n1 is None and n2 is None:
            return True

        if n1 is None or n2 is None or n1.val != n2.val:
            return False

        return self.isSameNode(n1.left, n2.left) and self.isSameNode(n1.right, n2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            node = stack.pop()

            if self.isSameNode(node, subRoot):
                return True

            if node is not None:
                stack.append(node.left)
                stack.append(node.right)

        return False


class Solution2:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return str(root).find(str(subRoot)) != -1
