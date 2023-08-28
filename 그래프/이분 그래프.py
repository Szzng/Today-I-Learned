# https://www.acmicpc.net/problem/1707


"""
이분 그래프
- 인접한 노드끼리 서로 다른 색으로 칠해서 모든 노드를 두 가지 색으로만 칠할 수 있는 그래프
- 인접한 노드끼리 같은 색으로 칠할 수 없는 그래프
- DFS로 탐색하며, 인접한 노드끼리 같은 색으로 칠해져 있는지 확인
"""


import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline


def dfs(v, group):
    global is_even

    if visited[v] == 0: # 방문하지 않은 노드만 group 지정
        visited[v] = group

    for child in graph[v]:
        if visited[child] == 0:
            dfs(child, visited[v] * -1)

        elif visited[child] == visited[v]:
            is_even = False
            return


k = int(read())

for _ in range(k):
    n, e = map(int, read().split())
    visited = [0] * (n + 1)
    is_even = True

    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1): # 모든 노드에 대해 dfs 수행: 그래프가 연결 그래프가 아니고 서로 끊어져 있을 수도 있으니까!
        if is_even:
            dfs(i, 1)
        else:
            break

    print("YES" if is_even else "NO")
