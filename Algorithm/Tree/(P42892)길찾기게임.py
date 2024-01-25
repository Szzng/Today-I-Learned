# https://school.programmers.co.kr/learn/courses/30/lessons/42892?language=python3
"""
# 문제
길찾기 게임은 카카오 프렌즈를 두 팀으로 나누고,
각 팀이 같은 곳을 다른 순서로 방문하도록 해서 먼저 순회를 마친 팀이 승리하는 것이다.

그냥 지도를 주고 게임을 시작하면 재미가 덜해지므로,
라이언은 방문할 곳의 2차원 좌표 값을 구하고 각 장소를 이진트리의 노드가 되도록 구성한 후,
순회 방법을 힌트로 주어 각 팀이 스스로 경로를 찾도록 할 계획이다.

라이언은 아래와 같은 특별한 규칙으로 트리 노드들을 구성한다.

- 트리를 구성하는 모든 노드의 x, y 좌표 값은 정수이다.
- 모든 노드는 서로 다른 x값을 가진다.
- 같은 레벨(level)에 있는 노드는 같은 y 좌표를 가진다.
- 자식 노드의 y 값은 항상 부모 노드보다 작다.
- 임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값보다 작다.
- 임의의 노드 V의 오른쪽 서브 트리(right subtree)에 있는 모든 노드의 x값은 V의 x값보다 크다.

이진트리에서 전위 순회(preorder), 후위 순회(postorder)를 한 결과가 각 팀이 방문해야 할 순서를 의미한다.
다행히 두 팀 모두 머리를 모아 분석한 끝에 라이언의 의도를 간신히 알아차렸다.
그러나 여전히 문제는 남아있다. 노드의 수가 쉽게 해결할 수 있겠지만, 예상대로 라이언은 그렇게 할 생각이 전혀 없었다.
곤경에 빠진 카카오 프렌즈를 위해 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수로 주어질 때,
노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return 하도록 solution 함수를 완성하자.

# 제한사항
nodeinfo는 이진트리를 구성하는 각 노드의 좌표가 1번 노드부터 순서대로 들어있는 2차원 배열이다.
nodeinfo의 길이는 1 이상 10,000 이하이다.
nodeinfo[i] 는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있다.
모든 노드의 좌표 값은 0 이상 100,000 이하인 정수이다.
트리의 깊이가 1,000 이하인 경우만 입력으로 주어진다.
모든 노드의 좌표는 문제에 주어진 규칙을 따르며, 잘못된 노드 위치가 주어지는 경우는 없다.

# 입력
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

# 출력
[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

# 시간복잡도:
"""

import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, num, x, y, left=None, right=None):
        self.num = num
        self.x = x
        self.y = y
        self.left = left
        self.right = right


def insert_node(parent, curr):
    if curr.x < parent.x:
        if parent.left:
            insert_node(parent.left, curr)
        else:
            parent.left = curr
    else:
        if parent.right:
            insert_node(parent.right, curr)
        else:
            parent.right = curr


def read_tree(nodeinfo):
    nodes = sorted([(idx + 1, x, y) for idx, (x, y) in enumerate(nodeinfo)], key=lambda n: (-n[2], n[1]))

    root = Node(*nodes[0])
    for node in nodes[1:]:
        # 재귀 버전
        insert_node(root, Node(*node))
        # 반복 버전
        # parent, curr = root, Node(*node)
        # while True:
        #     if curr.x < parent.x:
        #         if parent.left:
        #             parent = parent.left
        #         else:
        #             parent.left = curr
        #             break
        #     else:
        #         if parent.right:
        #             parent = parent.right
        #         else:
        #             parent.right = curr
        #             break

    return root


def preorder(root):
    if not root:
        return []

    return [root.num] + preorder(root.left) + preorder(root.right)


def postorder(root):
    if not root:
        return []

    return postorder(root.left) + postorder(root.right) + [root.num]


def solution(nodeinfo):
    root = read_tree(nodeinfo)
    return [preorder(root), postorder(root)]


assert (solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1],
                  [1, 3], [8, 6], [7, 2], [2, 2]])
        == [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]])
