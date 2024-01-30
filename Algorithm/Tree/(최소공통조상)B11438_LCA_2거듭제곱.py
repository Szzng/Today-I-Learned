# https://www.acmicpc.net/problem/11438

"""
# 문제
N(2 ≤ N ≤ 100,000)개의 정점으로 이루어진 트리가 주어진다.
트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.
두 노드의 쌍 M(1 ≤ M ≤ 100,000)개가 주어졌을 때,
두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

# 입력
첫째 줄에 노드의 개수 N이 주어지고,
다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다.
그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고,
다음 M개 줄에는 정점 쌍이 주어진다.

# 출력
M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.

# 시간제한: 1.5초
# 시간복잡도: O()

# 풀이
B11437번보다 N(노드의 개수)가 2배, M(쌍의 개수)가 10배 더 크지만 시간은 1/2로 줄어듦.
-> 제곱수 형태를 이용한 빠르게 최소 공통 조상을 구하는 방법을 사용해야 함.
"""

import sys
from collections import deque


class PowersLCA:
    def __init__(self, num_nodes):
        self.root = 1
        self.num_nodes = num_nodes
        self.tree = [[] for _ in range(self.num_nodes + 1)]

        for _ in range(self.num_nodes - 1):
            a, b = map(int, sys.stdin.readline().split())
            self.tree[a].append(b)
            self.tree[b].append(a)

        temp = 1
        self.k_max = 0
        while temp <= num_nodes:
            temp <<= 1
            self.k_max += 1

        self.parents = [[0] * (self.num_nodes + 1) for _ in range(self.k_max + 1)]
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

                    self.parents[0][next_node] = curr_node
                    self.depth[next_node] = self.depth[curr_node] + 1

        for k in range(1, self.k_max + 1):
            for node in range(1, self.num_nodes + 1):
                # 점화식으로 2의 거듭제곱 부모들 채우기
                self.parents[k][node] = self.parents[k - 1][self.parents[k - 1][node]]

    def get_lca(self, node1, node2):
        if self.depth[node1] < self.depth[node2]:
            node1, node2 = node2, node1  # node1이 무조건 더 깊은 노드가 되도록

        # 두 노드의 "깊이"가 같아질 때까지 더 깊은 노드를 위로 올림
        for k in range(self.k_max, -1, -1):
            if (1 << k) <= self.depth[node1] - self.depth[node2]:
                node1 = self.parents[k][node1]

        if node1 == node2:
            return node1

        # 두 노드가 같아질 때까지(두 노드가 같아지는 순간이 LCA) 두 노드를 2^k씩 동시에 위로 올림
        # 두 노드의 2^k번째 부모가 다른 경우 (self.parents[k][node1] != self.parents[k][node2])
        # 2^k번째 부모 레벨까지는 두 노드가 다른 경로에 있으며, 아직 LCA에 도달하지 않았음 -> 2^k번째 부모로 노드를 올리고 다시 탐색
        # 두 노드의 2^k번째 부모가 같은 경우 (self.parents[k][node1] == self.parents[k][node2])
        # 해당 2^k번째 조상이 LCA이거나 혹은 LCA보다 위쪽에 위치 -> k의 값을 줄여가며 더 작은 크기의 점프로 더 최소인 LCA를 찾으려 탐색을 계속함
        for k in range(self.k_max, -1, -1):
            if self.parents[k][node1] != self.parents[k][node2]:
                node1 = self.parents[k][node1]
                node2 = self.parents[k][node2]

        return self.parents[0][node1]


lca = PowersLCA(int(sys.stdin.readline()))

M = int(sys.stdin.readline())
memo = {}  # 같은 질문일 경우 재계산을 하지 않기 위해 딕셔너리 자료형 사용 -> 시간초과 해결 방법

for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())

    if (node1, node2) not in memo or (node2, node1) not in memo:
        memo[(node1, node2)] = memo[(node2, node1)] = lca.get_lca(node1, node2)  # 두 노드의 LCA를 딕셔너리에 저장

    print(memo[(node1, node2)])
