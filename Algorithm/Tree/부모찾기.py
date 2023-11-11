# https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

n = int(read())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parents = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(num):  #
    visited[num] = True

    for child in graph[num]:
        if not visited[child]:
            parents[child] = num  # 현재 노드를 부모로 설정
            dfs(child)


dfs(1)
print(*parents[2:], sep='\n')
