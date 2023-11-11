# https://www.acmicpc.net/problem/11657

"""
벨만-포드 알고리즘
- 한 노드에서 다른 모든 노드로 가는 최단 경로를 구하는 알고리즘

- 업데이트 조건
1. 간선이 잇는 출발 노드가 방문된 적이 있어야 한다. (dist[start] != sys.maxsize) : 출발 노드가 방문된 적이 없다 = 시작 노드(1번)에서 출발 노드로 가는 경로가 아직 없다. -> 갱신할 필요가 없다.
2. 출발 노드에서 도착 노드로 가는 비용이 출발 노드에서 도착 노드로 가는 비용보다 작아야 한다. (dist[end] > dist[start] + time)
"""

import sys

read = sys.stdin.readline

n, m = map(int, read().split())
edges = []
dist = [sys.maxsize] * (n + 1)

for _ in range(m):
    start, end, time = map(int, read().split())
    edges.append((start, end, time))

dist[1] = 0

# n개의 노드가 있을 때, 출발 노드에서 다른 모든 노드로 가는 최단 경로는 최대 n - 1개의 간선을 사용한다.
# 따라서 n - 1번의 간선을 모두 확인하면서 최소 비용을 갱신한다.
for _ in range(n - 1):
    for start, end, time in edges:
        if dist[start] != sys.maxsize and dist[end] > dist[start] + time:
            dist[end] = dist[start] + time

for start, end, time in edges:
    if dist[start] != sys.maxsize and dist[end] > dist[start] + time:  # 여전히 갱신이 되는 경우가 있다면 음수 사이클이 존재한다.
        print(-1)
        exit()

for i in range(2, n + 1):
    print(dist[i] if dist[i] != sys.maxsize else -1)
