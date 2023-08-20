# https://www.acmicpc.net/problem/13023

"""
- exit() : 프로그램 종료! 처음 알았음.

- !! visited[v] = False : 인접 리스트 내의 모든 요소를 방문했는데도 더 이상 방문할 곳이 없는 경우(= 조건을 충족시키지 못해 exit이 안된 경우), 방문 여부를 False로 초기화 !!
"""

import sys

sys.setrecursionlimit(10000)
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, depth):
    if depth == 4:
        print(1)
        exit()

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth + 1)

    # 인접 리스트 내의 모든 요소를 방문했는데도 exit은 안되었고, 더 이상 방문할 곳이 없는 경우
    # 방문 여부를 False로 초기화
    visited[v] = False


for i in range(n):
    dfs(i, 0)

print(0)
