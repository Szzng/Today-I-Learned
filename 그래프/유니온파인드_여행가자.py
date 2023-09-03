# https://www.acmicpc.net/problem/1976

import sys

sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

n = int(read())
m = int(read())

parent = [i for i in range(n + 1)]


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


for i in range(n):
    connect = list(map(int, read().split()))

    for j in range(n):
        if connect[j] == 1:
            union(i + 1, j + 1)

plan = list(map(int, read().split()))
standard = find(plan[0])
for i in range(1, m):
    if standard != find(plan[i]):
        print("NO")
        exit()

print('YES')
