# https://www.acmicpc.net/problem/2162


def ccw(p1, p2, p3):
    result = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])

    if result > 0:  # 반시계 방향
        return 1
    elif result < 0:  # 시계 방향
        return -1
    return 0  # 일직선


def is_overlap(p1, p2, p3, p4):
    if min(p1[0], p2[0]) <= max(p3[0], p4[0]) and min(p3[0], p4[0]) <= max(p1[0], p2[0]) and \
            min(p1[1], p2[1]) <= max(p3[1], p4[1]) and min(p3[1], p4[1]) <= max(p1[1], p2[1]):
        return True
    return False


def is_cross(p1, p2, p3, p4):
    result1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    result2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    if result1 == 0 and result2 == 0:
        return is_overlap(p1, p2, p3, p4)
    return result1 <= 0 and result2 <= 0


def find(a):  # a가 속한 집합의 루트 노드를 찾는 함수
    if parent[a] < 0:  # a가 루트 노드인 경우
        return a

    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a_parent = find(a)
    b_parent = find(b)

    if a_parent == b_parent:  # 이미 같은 집합인 경우
        return

    parent[a_parent] += parent[b_parent]  # a의 부모 노드에 b의 부모 노드 선분 개수를 더함
    parent[b_parent] = a_parent  # b_parent의 부모를 a_parent로 설정


import sys

read = sys.stdin.readline
n = int(read())
parent = [-1] * n

lines = [tuple(map(int, read().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if is_cross(lines[i][:2], lines[i][2:], lines[j][:2], lines[j][2:]):
            union(i, j)

cnt = 0
max_size = 0
for i in range(n):
    if parent[i] < 0:  # 루트 노드인 경우
        cnt += 1
        max_size = max(max_size, abs(parent[i]))

print(cnt)
print(max_size)
