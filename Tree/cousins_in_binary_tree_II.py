# https://leetcode.com/problems/cousins-in-binary-tree-ii/description/

from collections import Counter
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cnt = Counter()

        def get_vals_by_depth(node, depth):
            if not node: return
            cnt[depth] += node.val
            get_vals_by_depth(node.left, depth + 1)
            get_vals_by_depth(node.right, depth + 1)

        get_vals_by_depth(root, 0)

        def make_my_tree(node, depth, my_tree):
            children_cousin_sum = cnt[depth + 1] - (node.left.val if node.left else 0)- (node.right.val if node.right else 0)

            if node.left:
                my_tree.left = TreeNode(children_cousin_sum)
                make_my_tree(node.left, depth + 1, my_tree.left)

            if node.right:
                my_tree.right = TreeNode(children_cousin_sum)
                make_my_tree(node.right, depth + 1, my_tree.right)

            return my_tree

        return make_my_tree(root, 0, TreeNode(0))