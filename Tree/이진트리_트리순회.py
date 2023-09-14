# https://www.acmicpc.net/problem/1991

"""
- 전위 순회: 루트 -> 왼쪽 자식 -> 오른쪽 자식
- 중위 순회: 왼쪽 자식 -> 루트 -> 오른쪽 자식
- 후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 루트
"""

import sys

read = sys.stdin.readline

n = int(read())
tree = {}  # 트리를 딕셔너리로 구현

for _ in range(n):
    root, left, right = read().split()
    tree[root] = [left, right]


def preorder(root):
    if root == '.':
        return

    print(root, end='')  # 현재 노드
    preorder(tree[root][0])  # 왼쪽 자식 탐색
    preorder(tree[root][1])  # 오른쪽 자식 탐색


def inorder(root):
    if root == '.':
        return

    inorder(tree[root][0])  # 왼쪽 자식 탐색
    print(root, end='')  # 현재 노드
    inorder(tree[root][1])  # 오른쪽 자식 탐색


def postorder(root):
    if root == '.':
        return

    postorder(tree[root][0])  # 왼쪽 자식 탐색
    postorder(tree[root][1])  # 오른쪽 자식 탐색
    print(root, end='')  # 현재 노드


preorder('A')
print()
inorder('A')
print()
postorder('A')
