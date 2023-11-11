# https://www.acmicpc.net/problem/11404

import sys

read = sys.stdin.readline

n = int(read())
m = int(read())
graph = [[sys.maxsize if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, read().split())
    graph[start][end] = min(graph[start][end], cost)  # 중복되는 간선이 있을 수 있으므로 최소 비용을 저장해야 한다.

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):  # k: 거쳐가는 노드
    for i in range(1, n + 1):  # i: 출발 노드
        for j in range(1, n + 1):  # j: 도착 노드
            # 출발 노드에서 도착 노드로 가는 비용 vs 출발 노드에서 거쳐가는 노드를 거쳐 도착 노드로 가는 비용
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j] if graph[i][j] != sys.maxsize else 0, end=" ")
    print()
