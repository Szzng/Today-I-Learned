# https://school.programmers.co.kr/learn/courses/30/lessons/92343?language=python3

"""
# 문제
2진 트리 모양 초원의 각 노드에 늑대와 양이 한 마리씩 놓여 있습니다.
이 초원의 루트 노드에서 출발하여 각 노드를 돌아다니며 양을 모으려 합니다.
각 노드를 방문할 때 마다 해당 노드에 있던 양과 늑대가 당신을 따라오게 됩니다.
이때, 당신이 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 늑대는 바로 모든 양을 잡아먹어 버립니다.
당신은 중간에 양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아서 다시 루트 노드로 돌아오려 합니다.
루트 노드에는 항상 양이 있습니다.

각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열 info,
2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 edges가 매개변수로 주어질 때,
문제에 제시된 조건에 따라 각 노드를 방문하면서 모을 수 있는 양은 최대 몇 마리인지 return 하도록
solution 함수를 완성해주세요.

# 제한사항
2 ≤ info의 길이 ≤ 17
info의 원소는 0 또는 1 입니다.
info[i]는 i번 노드에 있는 양 또는 늑대를 나타냅니다.
0은 양, 1은 늑대를 의미합니다.
info[0]의 값은 항상 0입니다. 즉, 0번 노드(루트 노드)에는 항상 양이 있습니다.
edges의 세로(행) 길이 = info의 길이 - 1
edges의 가로(열) 길이 = 2
edges의 각 행은 [부모 노드 번호, 자식 노드 번호] 형태로, 서로 연결된 두 노드를 나타냅니다.
동일한 간선에 대한 정보가 중복해서 주어지지 않습니다.
항상 하나의 이진 트리 형태로 입력이 주어지며, 잘못된 데이터가 주어지는 경우는 없습니다.
0번 노드는 항상 루트 노드입니다.

# 입력
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

# 출력
result: 5

# 시간복잡도:
"""

from collections import deque


def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for parent, child in edges:
        tree[parent].append(child)

    # 현재 노드 위치, 양의 수, 늑대의 수, 방문 가능한 인접 노드 집합
    q = deque([(0, 1, 0, set())])
    max_sheep = 0

    while q:
        curr_node, cnt_sheep, cnt_wolf, next_nodes= q.popleft()
        max_sheep = max(cnt_sheep, max_sheep)

        next_nodes.update(tree[curr_node])  # 방문 노드 집합에 현재 노드의 자식 노드들 추가

        for next_node in next_nodes:
            if info[next_node] == 0:
                q.append((next_node, cnt_sheep + 1, cnt_wolf, next_nodes - {next_node}))
            elif cnt_sheep > cnt_wolf + 1:
                q.append((next_node, cnt_sheep, cnt_wolf + 1, next_nodes - {next_node}))

    return max_sheep


assert solution(
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
) == 5
assert solution(
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
) == 5
