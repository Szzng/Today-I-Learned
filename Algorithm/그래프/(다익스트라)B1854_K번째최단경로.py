# https://www.acmicpc.net/problem/1854

"""
# 문제
봄캠프를 마친 김조교는 여러 도시를 돌며 여행을 다닐 계획이다.
그런데 김 조교는, '느림의 미학'을 중요시하는 사람이라 항상 최단경로로만 이동하는 것은 별로 좋아하지 않는다.
하지만 너무 시간이 오래 걸리는 경로도 그리 매력적인 것만은 아니어서, 적당한 타협안인 'k번째 최단경로'를 구하길 원한다.
그를 돕기 위한 프로그램을 작성해 보자.

# 입력
첫째 줄에 n, m, k가 주어진다. (1 ≤ n ≤ 1000, 0 ≤ m ≤ 2,000,000, 1 ≤ k ≤ 100)
n과 m은 각각 김 조교가 여행을 고려하고 있는 도시들의 개수와, 도시 간에 존재하는 도로의 수이다.

이어지는 m개의 줄에는 각각 도로의 정보를 제공하는 세 개의 정수 a, b, c가 포함되어 있다.
이것은 a번 도시에서 b번 도시로 갈 때는 c의 시간이 걸린다는 의미이다. ( 1 ≤ a, b ≤ n, 1 ≤ c ≤ 1,000)

도시의 번호는 1번부터 n번까지 연속하여 붙어 있으며, 1번 도시는 시작 도시이다.
두 도로의 시작점과 도착점이 모두 같은 경우는 없다.

# 출력
n개의 줄을 출력한다.
i번째 줄에 1번 도시에서 i번 도시로 가는 k번째 최단경로의 소요시간을 출력한다.

경로의 소요시간은 경로 위에 있는 도로들을 따라 이동하는데 필요한 시간들의 합이다.
i번 도시에서 i번 도시로 가는 최단경로는 0이지만, 일반적인 k번째 최단경로는 0이 아닐 수 있음에 유의한다.

또, k번째 최단경로가 존재하지 않으면 -1을 출력한다.
최단경로에 같은 정점이 여러 번 포함되어도 된다.

# 시간제한: 2초
# 시간복잡도:

# 풀이
- 다익스트라 알고리즘을 사용하여 1번 노드에서 각 노드까지의 최단경로를 구한다.
- 이때, 각 노드까지의 최단경로를 저장하는 배열을 2차원 배열(k개의 row)로 선언한다.
- dist[i][j]: i번 노드까지 j번째로 최단경로로 도달하는 거리
- dist[i][k - 1]이 최단경로가 된다.
- k번째 경로를 찾기 위해 노드를 여러 번 방문하는 경우가 있으므로 기존 다익스트라의 방문 노드를 체크하여 재사용하지 않는 로직은 구현하지 않는다.
"""

import sys
from queue import PriorityQueue

read = sys.stdin.readline

num_nodes, num_edges, k = map(int, read().split())
start_node = 1

graph = [[] for _ in range(num_nodes + 1)]
for _ in range(num_edges):
    start, end, time = map(int, read().split())
    graph[start].append((time, end))

times = [[sys.maxsize] * k for _ in range(num_nodes + 1)]
visited = [0] * (num_nodes + 1)

q = PriorityQueue()
q.put((0, start_node))
times[start_node][0] = 0

while not q.empty():
    time_to_curr_node, curr_node = q.get()

    if visited[curr_node] == k:
        continue

    visited[curr_node] += 1

    for time_to_next_node, next_node in graph[curr_node]:
        new_time = time_to_curr_node + time_to_next_node

        if times[next_node][k - 1] <= new_time:
            continue

        times[next_node][k - 1] = new_time
        times[next_node].sort()
        q.put((new_time, next_node))

for i in range(1, num_nodes + 1):
    print(times[i][k - 1] if times[i][k - 1] != sys.maxsize else -1)
