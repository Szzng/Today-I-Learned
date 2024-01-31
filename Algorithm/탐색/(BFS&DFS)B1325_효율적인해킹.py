# https://www.acmicpc.net/problem/1325

"""
# 문제
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다.
이 회사는 N개의 컴퓨터로 이루어져 있다.
김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데,
A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때,
한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

# 입력
첫째 줄에, N과 M이 들어온다.
N은 10,000보다 작거나 같은 자연수,
M은 100,000보다 작거나 같은 자연수이다.

둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며,
"A가 B를 신뢰한다"를 의미한다.

컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

# 출력
첫째 줄에, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

# 시간제한: 5초
# 시간복잡도:
"""

import sys
from collections import deque


def make_graph(num_nodes, num_edges):
    graph = [[] for _ in range(num_nodes + 1)]

    for _ in range(num_edges):
        A, B = map(int, sys.stdin.readline().split())
        graph[B].append(A)

    return graph


def bfs_solution():
    def bfs(start_node):
        visited = [False] * (num_nodes + 1)
        cnt_node = 0
        queue = deque([start_node])
        visited[start_node] = True

        while queue:
            curr_node = queue.popleft()
            cnt_node += 1

            for next_node in graph[curr_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

        return cnt_node

    nums_children = [bfs(node) for node in range(1, num_nodes + 1)]
    max_num = max(nums_children)
    for node, num in enumerate(nums_children):
        if num == max_num:
            print(node + 1, end=" ")


def dfs_solution():
    def dfs(start_node):
        visited = [False] * (num_nodes + 1)
        cnt_node = 0
        stack = [start_node]
        visited[start_node] = True

        while stack:
            curr_node = stack.pop()
            cnt_node += 1

            for next_node in graph[curr_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    stack.append(next_node)

        return cnt_node

    nums_children = [dfs(node) for node in range(1, num_nodes + 1)]
    max_num = max(nums_children)
    for node, num in enumerate(nums_children):
        if num == max_num:
            print(node + 1, end=" ")


def dfs2_solution():
    sys.setrecursionlimit(10000)

    def dfs(start_node):
        visited = [False] * (num_nodes + 1)

        def _dfs(curr_node):
            visited[curr_node] = True
            cnt_node = 1

            for next_node in graph[curr_node]:
                if not visited[next_node]:
                    cnt_node += _dfs(next_node)

            return cnt_node

        return _dfs(start_node)

    nums_children = [dfs(node) for node in range(1, num_nodes + 1)]
    max_num = max(nums_children)
    for node, num in enumerate(nums_children):
        if num == max_num:
            print(node + 1, end=" ")


num_nodes, num_edges = map(int, sys.stdin.readline().split())
graph = make_graph(num_nodes, num_edges)

bfs_solution()
dfs_solution()
dfs2_solution()
