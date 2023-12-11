# https://www.acmicpc.net/problem/1260

def make_graph(node_cnt, edge_cnt):
    graph = [[] for _ in range(node_cnt + 1)]

    for _ in range(edge_cnt):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, node_cnt + 1):
        graph[i].sort()

    return graph


def make_visited(node_cnt):
    return [False] * (node_cnt + 1)


def dfs(graph, visited, node, dfs_result=[]):
    visited[node] = True
    dfs_result.append(node)

    for child in graph[node]:
        if not visited[child]:
            dfs(graph, visited, child, dfs_result)

    return dfs_result


def bfs(graph, visited, start_node):
    from collections import deque

    q = deque([start_node])
    visited[start_node] = True
    bfs_result = []

    while q:
        node = q.popleft()
        bfs_result.append(node)

        for child in graph[node]:
            if not visited[child]:
                q.append(child)
                visited[child] = True

    return bfs_result


import sys

read = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m, v = map(int, read().split())

graph = make_graph(n, m)

print(*dfs(graph, make_visited(n), v))
print(*bfs(graph, make_visited(n), v))
