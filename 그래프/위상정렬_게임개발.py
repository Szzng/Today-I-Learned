# https://www.acmicpc.net/problem/1516

"""
어떤 건물을 짓기 위해서 다른 건물을 먼저 지어야 할 수도 있다 -> 위상정렬
여러 개의 건물을 동시에 지을 수 있다. -> 동시에 지어지는 건물들은 순서를 고려하지 않는다.

최소 시간 = 각 건물을 짓는데 걸리는 시간 + 이전 건물을 짓는데 걸리는 시간 중 최대값 (이전 건물이 여러 개일 수 있음)
"""

import sys
from collections import deque

read = sys.stdin.readline

n = int(read())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, read().split()))
    time[i] = data[0]

    for x in data[1:]:
        if x == -1:
            break
        graph[x].append(i)
        indegree[i] += 1

q = deque([i for i in range(1, n + 1) if indegree[i] == 0])  # 진입차수가 0인 노드를 큐에 삽입

max_time = [0] * (n + 1) # 각 노드를 생산하기 위한 최대 시간

while q:
    now = q.popleft()

    for child in graph[now]:

        # 현재 노드의 최대 시간 vs 부모 노드의 최대 시간 + 부모 노드의 생산 시간 중 큰 값을 저장
        # 부모 노드가 여러 개일 수 있으므로 max_time[child]에는 최대값이 저장되어 있음
        max_time[child] = max(max_time[child], max_time[now] + time[now])

        indegree[child] -= 1  # 해당 노드와 연결된 간선 제거 (진입차수 1 감소)
        if indegree[child] == 0:  # 진입차수가 0이 되면 큐에 삽입
            q.append(child)

for i in range(1, n + 1):
    print(max_time[i] + time[i])  # 현재 노드의 최대 시간 + 현재 노드의 생산 시간
