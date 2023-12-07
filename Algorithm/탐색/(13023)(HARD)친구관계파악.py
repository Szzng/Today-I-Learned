# https://www.acmicpc.net/problem/13023

"""
# depth가 5인 경로가 존재하는지 확인하는 문제
# exit() : 프로그램 종료! 처음 알았음.

# dfs 함수에서 마지막에 visited[v] = False를 설정하는 이유
- 백트래킹(backtracking): 탐색 과정에서 더 이상 탐색이 불가능하거나 필요한 조건을 만족하지 못했을 때 이전 단계로 돌아가서 다른 경로를 탐색하는 방식
- 현재 정점 v에서 시작하는 모든 경로를 탐색한 후에는, v를 다시 방문하지 않은 상태로 되돌려 놓기 위해(다른 정점에서 시작할 때 v를 새로운 경로의 일부로 고려할 수 있도록)
- 인접 리스트 내의 모든 요소를 방문했는데도 더 이상 방문할 곳이 없는 경우(= 조건을 충족시키지 못해 exit이 안된 경우), 방문 여부를 False로 초기화
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
    if depth == 5:
        print(1)
        exit()

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth + 1)

    # 백트래킹
    visited[v] = False


# 모든 정점에 대한 dfs 실행
for i in range(n):
    dfs(i, 1)

print(0)
