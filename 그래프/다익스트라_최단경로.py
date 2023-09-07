# https://www.acmicpc.net/problem/1753

"""
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
"""

from queue import PriorityQueue
import sys

read = sys.stdin.readline

v, e = map(int, read().split())
start = int(read())

graph = [[] for _ in range(v + 1)]
dist = [sys.maxsize] * (v + 1)  # 각 노드를 방문했을 때의 최소 비용, 초기값은 무한대
visited = [False] * (v + 1)  # 방문 여부

for _ in range(e):
    a, b, w = map(int, read().split())
    graph[a].append((b, w))

q = PriorityQueue()
q.put((0, start))  # (비용, 노드)
dist[start] = 0

while not q.empty():
    cost, now = q.get()

    if not visited[now]:
        visited[now] = True

        for child, weight in graph[now]:
            # 현재 저장된 값 vs 부모 노드 최소 비용 + 부모 노드에서 자식 노드로 가는 비용 중 작은 값을 저장
            dist[child] = min(dist[child], dist[now] + weight)
            q.put((dist[child], child))

for i in range(1, v + 1):
    print(dist[i] if visited[i] else "INF")
