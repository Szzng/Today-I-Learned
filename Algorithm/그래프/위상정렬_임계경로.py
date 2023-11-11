# https://www.acmicpc.net/problem/1948

import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
m = int(read())
graph = [[] for _ in range(n + 1)]
reversed_graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    start, end, time = map(int, read().split())
    graph[start].append((end, time))
    reversed_graph[end].append((start, time))
    indegree[end] += 1

start, end = map(int, read().split())

q = deque([start])

result = [0] * (n + 1) # 각 노드를 방문했을 때의 최대 시간

while q:
    now = q.popleft()

    for child, time in graph[now]:
        # 현재 저장된 값 vs 부모 노드 최대 시간 + 부모 노드에서 자식 노드로 가는 시간 중 큰 값을 저장
        result[child] = max(result[child], result[now] + time)

        indegree[child] -= 1
        if indegree[child] == 0:
            q.append(child)
