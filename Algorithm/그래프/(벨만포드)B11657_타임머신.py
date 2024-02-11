# https://www.acmicpc.net/problem/11657

"""
# 문제
N개의 도시가 있다.
그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다.
각 버스는 A, B, C로 나타낼 수 있는데,
A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다.
시간 C가 양수가 아닌 경우가 있다.
C = 0인 경우는 순간 이동을 하는 경우,
C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.

1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 도시의 개수 N (1 ≤ N ≤ 500), 버스 노선의 개수 M (1 ≤ M ≤ 6,000)이 주어진다.
둘째 줄부터 M개의 줄에는 버스 노선의 정보 A, B, C (1 ≤ A, B ≤ N, -10,000 ≤ C ≤ 10,000)가 주어진다.

# 출력
만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력한다.
그렇지 않다면 N-1개 줄에 걸쳐 각 줄에 1번 도시에서 출발해 2번 도시, 3번 도시, ..., N번 도시로 가는 가장 빠른 시간을 순서대로 출력한다. 만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.


# 시간제한: 1초
# 시간복잡도:

# 풀이
- 시작점에서 다른 노드와 관련된 최단 거리를 구하는데, 에지가 음수가 가능할 때는 벨만-포드 알고리즘을 사용한다.
- 벨만-포드 알고리즘 : 한 노드에서 다른 모든 노드로 가는 최단 경로를 구하는 알고리즘
- 업데이트 조건
1. 출발 노드가 방문된 적 있어야 함 (distance[start] != sys.maxsize) : 출발 노드 방문된 적 X = 시작 노드(1번)에서 출발 노드로 가는 경로가 아직 X = 갱신할 필요 X
2. 출발 노드의 최단 거리 리스트 값 + 에지 가중치 < 도착 노드의 최단 거리 리스트값 (distance[end] > distance[start] + time)
"""
import sys


def read_edge_graph(num_edges):
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(num_edges)]

    return edges


def init_distance(num_nodes, start_node=1):
    distance = [sys.maxsize] * (num_nodes + 1)

    distance[start_node] = 0  # 시작 노드의 최단 거리는 0

    return distance


def relax_edges(num_nodes, edges, distance):
    # n개의 노드가 있을 때, 출발 노드에서 다른 모든 노드로 가는 최단 경로는 최대 n - 1개의 간선을 사용한다.
    # 따라서 n - 1번의 간선을 모두 확인하면서 최소 비용을 갱신한다.
    for _ in range(num_nodes - 1):
        for start, end, time in edges:
            if distance[start] != sys.maxsize and distance[start] + time < distance[end]:
                distance[end] = distance[start] + time


def detect_negative_cycle(edges, distance):
    for start, end, time in edges:
        # 여전히 갱신이 되는 경우가 있다면 음수 사이클이 존재한다.
        if distance[start] != sys.maxsize and distance[start] + time < distance[end]:
            return True
    return False


def print_distance(distance):
    for i in range(2, len(distance)):
        print(distance[i] if distance[i] != sys.maxsize else -1)


if __name__ == "__main__":
    num_nodes, num_edges = map(int, sys.stdin.readline().split())

    edges = read_edge_graph(num_edges)
    distance = init_distance(num_nodes)

    relax_edges(num_nodes, edges, distance)

    if detect_negative_cycle(edges, distance):
        print(-1)
    else:
        print_distance(distance)
