# https://www.acmicpc.net/problem/13023

"""
# depth가 5인 경로가 존재하는지 확인하는 문제
# exit() : 프로그램 종료! 처음 알았음.

# dfs_search_for_depth 함수에서 마지막에 visited[v] = False를 설정하는 이유
- 백트래킹(backtracking): 탐색 과정에서 더 이상 탐색이 불가능하거나 필요한 조건을 만족하지 못했을 때 이전 단계로 돌아가서 다른 경로를 탐색하는 방식
- 현재 정점 v에서 시작하는 모든 경로를 탐색한 후에는, v를 다시 방문하지 않은 상태로 되돌려 놓기 위해(다른 정점에서 시작할 때 v를 새로운 경로의 일부로 고려할 수 있도록)
- 인접 리스트 내의 모든 요소를 방문했는데도 더 이상 방문할 곳이 없는 경우(= 조건을 충족시키지 못해 exit이 안된 경우), 방문 여부를 False로 초기화
"""

import sys


def make_graph(n, m):
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    return graph


def dfs_search_for_depth(graph, v, depth, visited):
    if depth == 5:
        print(1)
        sys.exit(0)

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs_search_for_depth(graph, i, depth + 1, visited)

    # 백트래킹
    visited[v] = False


def main():
    sys.setrecursionlimit(10000)
    n, m = map(int, sys.stdin.readline().split())

    graph = make_graph(n, m)
    visited = [False] * n

    # 모든 정점에 대한 dfs 실행
    for i in range(n):
        dfs_search_for_depth(graph, i, 1, visited)

    print(0)


if __name__ == "__main__":
    main()
