# https://www.acmicpc.net/problem/1916

from queue import PriorityQueue
import sys

read = sys.stdin.readline

n = int(read())
m = int(read())

graph = [[] for _ in range(n + 1)]
dist = [sys.maxsize] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    start, end, cost = map(int, read().split())
    graph[start].append((end, cost))

start, end = map(int, read().split())

q = PriorityQueue()
q.put((0, start))
dist[start] = 0

while not q.empty():
    cost, now = q.get()

    if not visited[now]:
        visited[now] = True

        for child, weight in graph[now]:
            # 현재 저장된 값 vs 부모 노드 최소 비용 + 부모 노드에서 자식 노드로 가는 비용 중 작은 값을 저장
            dist[child] = min(dist[child], dist[now] + weight)
            q.put((dist[child], child))

print(dist[end])
