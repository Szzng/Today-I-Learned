# https://www.acmicpc.net/problem/1707

"""
# 이분 그래프
- 인접한 노드끼리 서로 다른 색으로 칠해서 모든 노드를 두 가지 색으로만 칠할 수 있는 그래프
- 인접한 노드끼리 같은 색으로 칠할 수 없는 그래프

# 문제
그래프의 정점의 집합을 둘로 분할하여,
각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

# 입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다.

각 테스트 케이스의 첫째 줄에는
그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다.
각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.

이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데,
각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.

2 ≤ K ≤ 5
1 ≤ V ≤ 20,000
1 ≤ E ≤ 200,000

# 출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.


# 시간제한: 2초
# 시간복잡도: O()
"""

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def make_graph():
    num_nodes, num_edges = map(int, read().split())
    graph = [[] for _ in range(num_nodes + 1)]

    for _ in range(num_edges):
        u, v = map(int, read().split())
        graph[u].append(v)
        graph[v].append(u)

    return graph


def bfs(start_node):
    q = deque([start_node])
    if group[start_node] == 0:
        group[start_node] = 1

    while q:
        curr_node = q.popleft()

        for next_node in graph[curr_node]:
            if group[next_node] == 0:
                group[next_node] = group[curr_node] * -1
                q.append(next_node)

            elif group[next_node] == group[curr_node]:
                return False
    return True


def dfs(start_node):
    if group[start_node] == 0:
        group[start_node] = 1

    def _dfs(curr_node):
        for next_node in graph[curr_node]:
            if group[next_node] == 0:
                group[next_node] = group[curr_node] * -1
                _dfs(next_node)

            elif group[next_node] == group[curr_node]:
                return False
        return True

    return _dfs(start_node)


read = sys.stdin.readline
for _ in range(int(read())):
    graph = make_graph()
    group = [0] * len(graph)
    FLAG = 'YES'

    # 모든 노드에 대해 bfs 수행
    # 그래프가 연결 그래프가 아니고 여러 개의 부분 그래프로 이루어져 있을 수 있기 때문
    for node in range(1, len(graph)):
        if not bfs(node):  # dfs(node)로 바꿔도 가능
            FLAG = 'NO'
            break

    print(FLAG)
