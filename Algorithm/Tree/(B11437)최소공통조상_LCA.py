# https://www.acmicpc.net/problem/11437

"""
# 문제
self.num_nodes(2 ≤ self.num_nodes ≤ 50,000)개의 정점으로 이루어진 트리가 주어진다.
트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.
두 노드의 쌍 M(1 ≤ M ≤ 10,000)개가 주어졌을 때,
두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

# 입력
첫째 줄에 노드의 개수 N이 주어지고,
다음 self.num_nodes-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다.
그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고,
다음 M개 줄에는 정점 쌍이 주어진다.

# 출력
M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.

# 시간제한: 3초
# 시간복잡도: O()
"""

import sys
from collections import deque


class LCA:
    def __init__(self, num_nodes):
        self.root = 1
        self.num_nodes = num_nodes
        self.tree = [[] for _ in range(self.num_nodes + 1)]

        for _ in range(self.num_nodes - 1):
            a, b = map(int, sys.stdin.readline().split())
            self.tree[a].append(b)
            self.tree[b].append(a)

        self.parent = [0] * (self.num_nodes + 1)
        self.depth = [0] * (self.num_nodes + 1)

        self.set_parent_and_depth()

    def set_parent_and_depth(self):
        visited = [False] * (self.num_nodes + 1)
        q = deque([self.root])
        visited[self.root] = True

        while q:
            curr_node = q.popleft()

            for next_node in self.tree[curr_node]:
                if not visited[next_node]:
                    q.append(next_node)
                    visited[next_node] = True

                    self.parent[next_node] = curr_node
                    self.depth[next_node] = self.depth[curr_node] + 1

    def get_lca(self, node1, node2):
        if self.depth[node1] < self.depth[node2]:
            node1, node2 = node2, node1  # node1이 무조건 더 깊은 노드가 되도록

        # 두 노드의 "깊이"가 같아질 때까지 더 깊은 노드를 위로 올림
        while self.depth[node1] != self.depth[node2]:
            node1 = self.parent[node1]

        # 두 노드가 같아질 때까지(두 노드가 같아지는 순간이 LCA) 두 노드를 동시에 위로 올림
        while node1 != node2:
            node1 = self.parent[node1]
            node2 = self.parent[node2]

        return node1


lca = LCA(int(sys.stdin.readline()))

M = int(sys.stdin.readline())
memo = {}  # 같은 질문일 경우 재계산을 하지 않기 위해 딕셔너리 자료형 사용 -> 시간초과 해결 방법

for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())

    if (node1, node2) not in memo or (node2, node1) not in memo:
        memo[(node1, node2)] = memo[(node2, node1)] = lca.get_lca(node1, node2)  # 두 노드의 LCA를 딕셔너리에 저장

    print(memo[(node1, node2)])
