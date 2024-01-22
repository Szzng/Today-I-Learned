class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node

        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            # 자식 노드가 하나인 경우: 자식 노드를 삭제된 노드의 위치로 이동
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 자식 노드가 두개인 경우
            # 삭제하려는 노드의 오른쪽 서브트리에서 가장 작은 값을 가진 노드(가장 왼쪽 노드)를 찾아서
            # 그 값을 삭제하려는 노드 위치에 복사하고
            # 오른쪽 서브트리에서는 그 노드를 삭제한다.
            node.val = self._min_value_node(node.right).val
            node.right = self._delete(node.right, node.val)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.val, end=' ')
            self._inorder(node.right)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(node.val, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.val, end=' ')


bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("In-order Traversal:")
bst.inorder()

print("Pre-order Traversal:")
bst.preorder()

print("Post-order Traversal:")
bst.postorder()
