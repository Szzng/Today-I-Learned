# https://www.acmicpc.net/problem/1389

import sys

read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[sys.maxsize if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, read().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):  # k: 거쳐가는 노드
    for i in range(1, n + 1):  # i: 출발 노드
        for j in range(1, n + 1):  # j: 도착 노드
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_bacon = sys.maxsize
min_bacon_user = 0

for i in range(1, n + 1):
    bacon = sum(graph[i][1:])
    if min_bacon > bacon:
        min_bacon = bacon
        min_bacon_user = i

print(min_bacon_user)
