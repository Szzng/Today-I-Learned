"""
- 전위 순회: 부모 -> 왼쪽 자식 -> 오른쪽 자식
- 중위 순회: 왼쪽 자식 -> 부모 -> 오른쪽 자식
- 후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 부모
"""


def preorder(nodes, idx):
    if idx >= len(nodes):
        return ""

    ret = str(nodes[idx]) + " "
    ret += preorder(nodes, idx * 2 + 1)
    ret += preorder(nodes, idx * 2 + 2)
    return ret


def inorder(nodes, idx):
    if idx >= len(nodes):
        return ""

    ret = inorder(nodes, idx * 2 + 1)
    ret += str(nodes[idx]) + " "
    ret += inorder(nodes, idx * 2 + 2)
    return ret


def postorder(nodes, idx):
    if idx >= len(nodes):
        return ""

    ret = postorder(nodes, idx * 2 + 1)
    ret += postorder(nodes, idx * 2 + 2)
    ret += str(nodes[idx]) + " "
    return ret


def solution(nodes):
    return [
        preorder(nodes, 0)[:-1],  # 마지막 공백 제거
        inorder(nodes, 0)[:-1],  # 마지막 공백 제거
        postorder(nodes, 0)[:-1],  # 마지막 공백 제거
    ]


print(solution([1, 2, 3, 4, 5, 6, 7]) == ["1 2 4 5 3 6 7", "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"])
