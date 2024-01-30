# https://www.acmicpc.net/problem/11724

"""
# 그래프의 연결 요소(Connected Component)
- 그래프 내에서 서로 도달 가능한 정점들의 집합
- 무방향 그래프에서, 모든 정점이 경로로 서로 연결되어 있는 최대 부분 그래프
-> 연결 요소의 개수를 구한다 = 분리되어 있는 그래프의 개수를 구한다

# sys.setrecursionlimit
- 파이썬의 재귀 최대 깊이의 기본 설정은 1000회 -> 재귀 호출의 깊이가 파이썬의 기본 재귀 깊이 한계를 초과하면 RecursionError 발생
- sys.setrecursionlimit 함수는 파이썬에서 재귀 호출의 최대 깊이 한계를 조정하는 데 사용
- 재귀 깊이 한계를 너무 높게 설정하면 스택 오버플로우가 발생할 수 있음.
- 가능한 경우 재귀 대신 반복문을 사용하거나, 꼬리 재귀(Tail Recursion)와 같은 최적화 기법을 적용하는 것이 좋음.


# 문제 입력
- 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
- 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다
"""

import sys

sys.setrecursionlimit(10000)  # 재귀 깊이 설정
read = sys.stdin.readline  # 이거 안하면 시간초과


def make_graph(n, m):
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, read().split())
        graph[u].append(v)
        graph[v].append(u)

    return graph


def dfs(node):
    visited[node] = True

    for child in graph[node]:
        if not visited[child]:
            dfs(child)


n, m = map(int, read().split())

graph = make_graph(n, m)
visited = [False] * (n + 1)

connected_component_cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        connected_component_cnt += 1
        dfs(i)

print(connected_component_cnt)
