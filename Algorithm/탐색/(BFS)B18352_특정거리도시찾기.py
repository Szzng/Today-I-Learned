# https://www.acmicpc.net/problem/18352

"""
# 문제
어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다.
모든 도로의 거리는 1이다.

이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서,
최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

# 입력
첫째 줄에 도시의 개수 N, (2 ≤ N ≤ 300,000)
도로의 개수 M, (1 ≤ M ≤ 1,000,000)
거리 정보 K,(1 ≤ K ≤ 300,000)
출발 도시의 번호 X가 주어진다. (1 ≤ X ≤ N)

둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다.
이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N)
단, A와 B는 서로 다른 자연수이다.

# 출력
X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

# 시간제한: 2초
# 시간복잡도:
"""

import sys
from collections import deque


def make_graph(num_nodes, num_edges):
    graph = [[] for _ in range(num_nodes + 1)]

    for _ in range(num_edges):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)

    return graph


def bfs(graph, start_node):
    # visited와 distance를 함께 처리하기 위해 -1로 초기화(-1이면 방문하지 않은 노드)
    distance = [-1] * len(graph)

    queue = deque([start_node])
    distance[start_node] = 0

    while queue:
        curr_node = queue.popleft()

        for next_node in graph[curr_node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[curr_node] + 1
                queue.append(next_node)

    return distance


def solution():
    num_nodes, num_edges, target_dist, start_node = map(int, sys.stdin.readline().split())
    graph = make_graph(num_nodes, num_edges)
    distance = bfs(graph, start_node)

    answer = sorted([idx for idx, dist in enumerate(distance) if dist == target_dist])
    print(*answer, sep="\n") if answer else print(-1)


if __name__ == '__main__':
    solution()
