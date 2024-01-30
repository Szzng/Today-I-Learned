# https://school.programmers.co.kr/learn/courses/30/lessons/68937?language=python3

"""
# 문제
n개의 점으로 이루어진 트리가 있습니다.
이때, 트리 상에서 다음과 같은 것들을 정의합니다.

어떤 두 점 사이의 거리는, 두 점을 잇는 경로 상 간선의 개수로 정의합니다.
임의의 3개의 점 a, b, c에 대한 함수 f(a, b, c)의 값을 a와 b 사이의 거리, b와 c 사이의 거리, c와 a 사이의 거리, 3개 값의 중간값으로 정의합니다.

트리의 정점의 개수 n과 트리의 간선을 나타내는 2차원 정수 배열 edges가 매개변수로 주어집니다.
주어진 트리에서 임의의 3개의 점을 뽑아 만들 수 있는 모든 f값 중에서,
제일 큰 값을 구해 return 하도록 solution 함수를 완성해주세요.

# 제한사항
n은 3 이상 250,000 이하입니다.
edges의 행의 개수는 n-1 입니다.
edges의 각 행은 [v1, v2] 2개의 정수로 이루어져 있으며, 이는 v1번 정점과 v2번 정점 사이에 간선이 있음을 의미합니다.
v1, v2는 각각 1 이상 n 이하입니다.
v1, v2는 다른 수입니다.
입력으로 주어지는 그래프는 항상 트리입니다.


# 입출력 예
n	edges	result
4	[[1,2],[2,3],[3,4]]	2
5	[[1,5],[2,5],[3,5],[4,5]]	2

# 시간복잡도:
"""

import sys

sys.setrecursionlimit(10 ** 6)


def read_tree(n, edges):
    tree = [[] for _ in range(n + 1)]

    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    return tree


def dfs(tree, node):
    def _dfs(node):
        visited[node] = True

        for next_node in tree[node]:
            if not visited[next_node]:
                distances[next_node] = distances[node] + 1
                _dfs(next_node)

    visited = [False] * len(tree)
    distances = [0] * len(tree)
    _dfs(node)

    max_distance = max(distances)
    farthest_nodes = [i for i, distance in enumerate(distances) if distance == max_distance]

    return farthest_nodes, max_distance


def solution(n, edges):
    tree = read_tree(n, edges)

    farthest_nodes, _ = dfs(tree, 1)
    farthest_nodes2, tree_diameter = dfs(tree, farthest_nodes[0])

    if len(farthest_nodes2) > 1:
        return tree_diameter

    else:
        farthest_nodes3, tree_diameter = dfs(tree, farthest_nodes2[0])
        return tree_diameter if len(farthest_nodes3) > 1 else tree_diameter - 1


assert solution(4, [[1, 2], [2, 3], [3, 4]]) == 2
assert solution(5, [[1, 5], [2, 5], [3, 5], [4, 5]]) == 2
