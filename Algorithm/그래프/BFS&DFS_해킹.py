# https://www.acmicpc.net/problem/1325


"""
이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

- 가장 많이 신뢰받는 컴퓨터를 해킹하면 되는 문제
"""


def bfs_solution():
    def bfs(v):  # v번 컴퓨터를 해킹했을 때 신뢰받는 컴퓨터의 수를 반환
        q = deque([v])
        visited = [False] * (n + 1)
        visited[v] = True
        count = 0

        while q:
            now = q.popleft()
            count += 1

            for child in graph[now]:
                if not visited[child]:
                    visited[child] = True
                    q.append(child)

        return count

    return [0] + [bfs(i) for i in range(1, n + 1)]  # 0번 컴퓨터는 없으므로 0을 미리 넣어줌


def dfs_solution():
    sys.setrecursionlimit(10000)

    def dfs(v):  # v번 컴퓨터를 해킹했을 때 신뢰받는 컴퓨터의 수를 반환
        visited = [False] * (n + 1)
        visited[v] = True
        count = 1

        for child in graph[v]:
            if not visited[child]:
                visited[child] = True
                count += dfs(child) # dfs(child)를 호출하면 child를 해킹했을 때 신뢰받는 컴퓨터의 수를 반환받음

        return count

    return [0] + [dfs(i) for i in range(1, n + 1)]  # 0번 컴퓨터는 없으므로 0을 미리 넣어줌


import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, read().split())
    graph[b].append(a)

# answer = bfs_solution()
answer = dfs_solution()

max_value = max(answer)

for i in range(1, n + 1):
    if answer[i] == max_value:
        print(i, end=" ")
