# https://www.acmicpc.net/problem/11724

"""
- 그래프의 연결 요소 : 그래프에서 정점의 개수 (분리되어 있는 그래프의 수)
- sys.setrecursionlimit: 파이썬의 재귀 최대 깊이의 기본 설정은 1000회이기 때문에 런타임 에러가 발생하지 않도록 최대 깊이를 늘여준다
"""

import sys

sys.setrecursionlimit(10000)  # 재귀 깊이 설정
read = sys.stdin.readline

n, m = map(int, read().split())

adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    s, e = map(int, read().split())
    adj[s].append(e)
    adj[e].append(s)


def dfs(v):
    visited[v] = True

    for u in adj[v]:
        if not visited[u]:
            dfs(u)


count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
