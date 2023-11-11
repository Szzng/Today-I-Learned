# https://www.acmicpc.net/problem/18352


import sys
from collections import deque

read = sys.stdin.readline

n, m, k, x = map(int, read().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)

distances = [-1] * (n + 1)


def bfs(v):
    q = deque([v])
    distances[v] = 0

    while q:
        curr_node = q.popleft()
        for next_node in graph[curr_node]:
            if distances[next_node] == -1:
                distances[next_node] = distances[curr_node] + 1
                q.append(next_node)


bfs(x)

answer = [i for i in range(1, n + 1) if distances[i] == k]

if answer:
    answer.sort()
    print(*answer, sep="\n")
else:
    print(-1)
