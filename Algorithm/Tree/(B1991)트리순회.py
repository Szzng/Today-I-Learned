# https://www.acmicpc.net/problem/1991

"""
# 문제
이진 트리를 입력받아
전위 순회(preorder traversal),
중위 순회(inorder traversal),
후위 순회(postorder traversal)한
결과를 출력하는 프로그램을 작성하시오.

# 입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
자식 노드가 없는 경우에는 .으로 표현한다.

# 출력
첫째 줄에 전위 순회,
둘째 줄에 중위 순회,
셋째 줄에 후위 순회한 결과를 출력한다.
각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

# 시간제한: 2초
# 시간복잡도:

# 풀이
- 전위 순회: 부모 -> 왼쪽 자식 -> 오른쪽 자식
- 중위 순회: 왼쪽 자식 -> 부모 -> 오른쪽 자식
- 후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 부모
"""
import sys

num_nodes = int(sys.stdin.readline())
tree = {}  # 트리를 딕셔너리로 구현

for _ in range(num_nodes):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]


def preorder(parent_node):
    if parent_node == '.':
        return

    print(parent_node, end='')  # 현재 노드
    preorder(tree[parent_node][0])  # 왼쪽 자식 탐색
    preorder(tree[parent_node][1])  # 오른쪽 자식 탐색


def inorder(parent_node):
    if parent_node == '.':
        return

    inorder(tree[parent_node][0])  # 왼쪽 자식 탐색
    print(parent_node, end='')  # 현재 노드
    inorder(tree[parent_node][1])  # 오른쪽 자식 탐색


def postorder(parent_node):
    if parent_node == '.':
        return

    postorder(tree[parent_node][0])  # 왼쪽 자식 탐색
    postorder(tree[parent_node][1])  # 오른쪽 자식 탐색
    print(parent_node, end='')  # 현재 노드


preorder('A')
print()
inorder('A')
print()
postorder('A')
