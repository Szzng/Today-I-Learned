# https://www.acmicpc.net/problem/2252

"""
- 답이 여러가지인 경우 아무거나 출력해도 된다. -> 위상정렬
- - 진입차수란 특정한 노드로 들어오는 간선의 개수를 의미한다. (A -> B로 이동하는 간선이 존재한다면, B의 진입차수는 1 증가한다.)
"""

from collections import deque
import sys
read = sys.stdin.readline

n, m = map(int, read().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1) # 진입차수

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)

    indegree[b] += 1 # 진입차수 1 증가

q = deque([i for i in range(1, n+1) if indegree[i] == 0]) # 진입차수가 0인 노드를 큐에 삽입

while q:
    now = q.popleft()
    print(now, end=' ')

    for child in graph[now]:
        indegree[child] -= 1 # 해당 노드와 연결된 간선 제거 (진입차수 1 감소)
        if indegree[child] == 0: # 진입차수가 0이 되면 큐에 삽입
            q.append(child)
