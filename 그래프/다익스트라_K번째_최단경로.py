# https://www.acmicpc.net/problem/1854

"""
- 다익스트라 알고리즘을 사용하여 1번 노드에서 각 노드까지의 최단경로를 구한다.
- 이때, 각 노드까지의 최단경로를 저장하는 배열을 2차원 배열(k개의 row)로 선언한다.
- dist[i][j]: i번 노드까지 j번째로 최단경로로 도달하는 거리
- dist[i][k - 1]이 최단경로가 된다.
- k번째 경로를 찾기 위해 노드를 여러 번 방문하는 경우가 있으므로 기존 다익스트라의 방문 노드를 체크하여 재사용하지 않는 로직은 구현하지 않는다.
"""

from queue import PriorityQueue
import sys

read = sys.stdin.readline

n, m, k = map(int, read().split())
graph = [[] for _ in range(n + 1)]
dist = [[float('inf')] * k for _ in range(n + 1)]  # dist[i][j]: i번 노드까지 j번째로 최단경로로 도달하는 거리

for _ in range(m):
    start, end, cost = map(int, read().split())
    graph[start].append((end, cost))

q = PriorityQueue()
q.put((0, 1))  # (cost, node)
dist[1][0] = 0  # 1번 노드까지 0번째로 최단경로로 도달하는 거리는 0

while not q.empty():
    cost, now = q.get()

    for child, child_cost in graph[now]:
        new_cost = cost + child_cost

        if dist[child][k - 1] > new_cost:
            dist[child][k - 1] = new_cost
            dist[child].sort()
            q.put((new_cost, child))

for i in range(1, n + 1):
    if dist[i][k - 1] == float('inf'):
        print(-1)
    else:
        print(dist[i][k - 1])
