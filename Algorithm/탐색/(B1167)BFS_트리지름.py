# https://www.acmicpc.net/problem/1167

"""
# 트리의 지름 : 트리에서 두 노드 간 가장 긴 경로의 길이
1. 임의의 노드에서 가장 먼 노드 찾기
2. 찾은 노드에서 다시 가장 먼 노드 찾기

# 임의의 노드에서 가장 긴 경로로 연결되어 있는 노드는 트리의 지름에 반드시 포함됨.
- 트리는 사이클이 없는 연결 그래프이므로, 두 노드 사이에는 항상 하나의 유일한 경로가 존재합니다.
- 따라서 처음에 임의의 노드에서 가장 멀리 있는 노드를 찾았을 때, 그 노드는 지름을 형성하는 경로의 한 끝점이 됩니다.
- 그리고 그 끝점에서 가장 멀리 있는 노드까지의 경로가 바로 트리의 최대 길이, 즉 지름이 됩니다.
"""

import sys
from collections import deque


def make_graph():
    v = int(sys.stdin.readline())
    graph = [[] for _ in range(v + 1)]

    for _ in range(v):
        info = list(map(int, sys.stdin.readline().split()))
        node = info[0]
        for i in range(1, len(info) - 1, 2):
            graph[node].append((info[i], info[i + 1]))

    return graph


def bfs(graph, start_node):
    q = deque()
    visited = [False] * (len(graph) + 1)
    distances = [0] * (len(graph) + 1)

    q.append(start_node)
    visited[start_node] = True

    while q:
        current = q.popleft()

        for neighbor, dist in graph[current]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
                distances[neighbor] = distances[current] + dist

    return distances


graph = make_graph()
farthest_distances = bfs(graph, 1)
farthest_node = farthest_distances.index(max(farthest_distances))
print(max(bfs(graph, farthest_node)))
