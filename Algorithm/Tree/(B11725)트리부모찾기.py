# https://www.acmicpc.net/problem/11725

"""
# 문제
루트 없는 트리가 주어진다.
이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

# 시간제한: 1초
# 시간복잡도: O(N)
"""

import sys
from typing import List

sys.setrecursionlimit(10 ** 6)


def read_tree_edges(num_nodes: int) -> List[List[int]]:
    graph = [[] for _ in range(num_nodes + 1)]

    for _ in range(num_nodes - 1):
        node1, node2 = map(int, sys.stdin.readline().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph


def find_parents(num_nodes: int, graph: List[List[int]]) -> List[int]:
    parents = [0] * (num_nodes + 1)
    visited = [False] * (num_nodes + 1)

    def dfs(curr_node: int):
        visited[curr_node] = True

        for next_node in graph[curr_node]:
            if not visited[next_node]:
                parents[next_node] = curr_node
                dfs(next_node)

    dfs(1)
    return parents


num_nodes = int(sys.stdin.readline())
graph = read_tree_edges(num_nodes)
parents = find_parents(num_nodes, graph)
print(*parents[2:], sep='\n')
