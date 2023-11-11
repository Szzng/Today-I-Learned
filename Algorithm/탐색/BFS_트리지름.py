# https://www.acmicpc.net/problem/1167

"""
- 트리의 지름 : 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것
- 임의의 노드에서 가장 거리가 먼 노드를 구하고, 그 노드에서 가장 거리가 먼 노드를 구하면 트리의 지름을 구할 수 있음
- 임의의 노드에서 가장 긴 경로로 연결되어 있는 노드는 트리의 지름에 반드시 포함됨
"""

import sys
from collections import deque

read = sys.stdin.readline
v = int(read())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    info = list(map(int, read().split()))
    node = info[0]
    for i in range(1, len(info) - 1, 2):
        graph[node].append((info[i], info[i + 1]))


def bfs(num):
    q = deque([num])
    visited[num] = True

    while q:
        now = q.popleft()
        for node, distance in graph[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                distances[node] = distances[now] + distance


distances = [0] * (v + 1)
visited = [False] * (v + 1)
bfs(1)
max_idx = distances.index(max(distances))

distances = [0] * (v + 1)
visited = [False] * (v + 1)
bfs(max_idx)
print(max(distances))
