# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

sys.setrecursionlimit(10000)
read = sys.stdin.readline

n, m, v = map(int, read().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dfs_result = []
bfs_result = []

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()


def dfs(num):
    visited[num] = True
    dfs_result.append(str(num))

    for i in graph[num]:
        if not visited[i]:
            dfs(i)


def bfs(num):
    global bfs_result

    q = deque([num])
    visited[num] = True

    while q:
        now = q.popleft()
        bfs_result.append(str(now))

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(v)
print(' '.join(dfs_result))

visited = [False] * (n + 1)
bfs(v)
print(' '.join(bfs_result))
