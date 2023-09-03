# https://www.acmicpc.net/problem/1717

import sys

sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

n, m = map(int, read().split())
parent = [i for i in range(n + 1)]


def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])  # 루트 노드를 찾아서 갱신하여 경로 압축
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

def is_same_parent(x, y):
    return find(x) == find(y)


for _ in range(m):
    op, a, b = map(int, read().split())
    if op == 0:
        union(a, b)
    else:
        if is_same_parent(a, b):
            print('YES')
        else:
            print('NO')
