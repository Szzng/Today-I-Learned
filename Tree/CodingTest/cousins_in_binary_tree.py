# https://leetcode.com/problems/cousins-in-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        record = {root.val: (0, None)}

        def record_node(node, depth):
            if node is None: return

            record_node(node.left, depth + 1)
            record_node(node.right, depth + 1)

            if node.left is not None:
                record[node.left.val] = (depth + 1, node.val)

            if node.right is not None:
                record[node.right.val] = (depth + 1, node.val)

        record_node(root, 0)

        return (record[x][0] == record[y][0]) and (record[x][1] != record[y][1])


class Solution2:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        record = {root.val: (0, None)}
        nodes = [(root, 0)]

        while nodes:
            node, depth = nodes.pop(0)
            if node is None: continue

            nodes.append([node.left, depth + 1])
            nodes.append([node.right, depth + 1])

            if node.left is not None:
                record[node.left.val] = (depth + 1, node.val)

            if node.right is not None:
                record[node.right.val] = (depth + 1, node.val)

            if (x in record) and (y in record):
                return (record[x][0] == record[y][0]) and (record[x][1] != record[y][1])

        return (record[x][0] == record[y][0]) and (record[x][1] != record[y][1])
