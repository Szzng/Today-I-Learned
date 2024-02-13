# https://www.acmicpc.net/problem/1197

"""
# 문제
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

# 입력
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다.
다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다.
이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다.
C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다.
최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

# 출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

# 시간제한: 1초
# 시간복잡도:
"""
import sys


class UnionFind:  # 유니온파인드로 사이클 생성 여부를 판단
    def __init__(self, num_nodes):
        self.parent = [i for i in range(num_nodes + 1)]

    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:  # 두 정점의 부모가 같지 않다면 연결 (부모가 같은데 연결하면 사이클이 생김)
            self.parent[root_y] = root_x
            return True

        return False


num_nodes, num_edges = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(num_edges)]
edges.sort(key=lambda x: x[2])  # 가중치 기준으로 오름차순 정렬

used_edges = 0  # 사용한 에지의 수
total_weight = 0  # 총 가중치
uf = UnionFind(num_nodes)

for node1, node2, weight in edges:
    if used_edges == num_nodes - 1:  # 모든 정점을 연결했다면
        break

    if uf.union(node1, node2):
        total_weight += weight
        used_edges += 1

print(total_weight)
