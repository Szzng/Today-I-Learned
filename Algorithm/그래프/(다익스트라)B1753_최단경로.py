# https://www.acmicpc.net/problem/1753

"""
# 문제
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
단, 모든 간선의 가중치는 10 이하의 자연수이다.

# 입력
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.

둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다.

셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다.
u와 v는 서로 다르며 w는 10 이하의 자연수이다.

서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

# 출력
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.
시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

# 시간제한: 1초
# 시간복잡도:
"""

import sys
from queue import PriorityQueue

read = sys.stdin.readline

num_nodes, num_edges = map(int, read().split())
start_node = int(input())
graph = [[] for _ in range(num_nodes + 1)]
distance = [sys.maxsize] * (num_nodes + 1)  # 각 노드를 방문했을 때의 최소 거리, 초기값은 무한대
visited = [False] * (num_nodes + 1)  # 방문 여부

for _ in range(num_edges):
    start, end, weight = map(int, read().split())
    graph[start].append((end, weight))

q = PriorityQueue()
q.put((0, start_node))  # (거리, 노드) -> 자동으로 거리가 작은 순으로 정렬됨
distance[start_node] = 0

while not q.empty():
    _, curr_node = q.get()

    if visited[curr_node]:
        continue

    visited[curr_node] = True

    for next_node, weight in graph[curr_node]:
        # 현재 저장된 값 vs (부모 노드 최소 거리 + 부모 노드에서 자식 노드로 가는 가중치) 중 작은 값을 저장
        distance[next_node] = min(distance[next_node], distance[curr_node] + weight)
        q.put((distance[next_node], next_node))

for i in range(1, num_nodes + 1):
    print(distance[i] if visited[i] else "INF")
