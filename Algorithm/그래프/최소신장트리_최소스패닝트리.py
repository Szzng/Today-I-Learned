# https://www.acmicpc.net/problem/1197

"""
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.
"""

from queue import PriorityQueue
import sys

read = sys.stdin.readline

v, e = map(int, read().split())
parent = [i for i in range(v + 1)]  # 사이클 생성 여부를 판단하기 위한 유니온 파인드용 부모 리스트


def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x


edges = PriorityQueue()  # 최소 신장 트리는 에지 중심의 알고리즘이므로 데이터를 에지 리스트로 저장
for _ in range(e):
    a, b, c = map(int, read().split())
    edges.put((c, a, b))  # 에지의 가중치를 기준으로 정렬하기 위해 가중치를 맨 앞에 둠 (가중치, 정점1, 정점2)

use_edges = 0  # 사용한 에지의 수
total_weight = 0  # 총 가중치

while use_edges < v - 1:  # 사용한 에지의 수가 정점의 수 - 1이 될 때까지 반복 (최소신장트리는 정점의 수 - 1개의 에지로 구성됨)
    weight, a, b = edges.get()  # 가중치가 가장 작은 에지를 꺼냄

    if find(a) != find(b):  # 두 정점의 부모가 같지 않다면 (사이클이 생성되지 않는다면)
        union(a, b)  # 두 정점을 연결
        total_weight += weight  # 가중치를 더함
        use_edges += 1  # 사용한 에지의 수를 더함

print(total_weight)
