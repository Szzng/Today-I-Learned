# https://www.acmicpc.net/problem/1260

from collections import deque
import sys


def create_graph(node_cnt, edge_cnt):
    graph = [[] for _ in range(node_cnt + 1)]

    for _ in range(edge_cnt):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, node_cnt + 1):
        graph[i].sort()

    return graph


def init_visited(node_cnt):
    return [False] * (node_cnt + 1)


def dfs(graph, node, visited=None):
    if not visited:
        visited = init_visited(len(graph))

    visited[node] = True
    result = [node]

    for child in graph[node]:
        if not visited[child]:
            result += dfs(graph, child, visited)

    return result


def bfs(graph, start_node):
    q = deque([start_node])
    visited = init_visited(len(graph))
    visited[start_node] = True
    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for child in graph[node]:
            if not visited[child]:
                q.append(child)
                visited[child] = True

    return result


def main():
    n, m, v = map(int, sys.stdin.readline().split())
    graph = create_graph(n, m)

    sys.setrecursionlimit(10000)
    print(*dfs(graph, v))
    print(*bfs(graph, v))


if __name__ == "__main__":
    main()
