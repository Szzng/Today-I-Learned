# https://www.acmicpc.net/problem/17387


"""
선분 AB와 CD가 교차하는지 확인하는 방법

- 교차점이 생기는 경우
    - 선분 AB와 선분 CD가 교차하려면, 선분 AB의 양 끝점 A, B가 선분 CD의 양 끝점 C, D의 다른 쪽에 있어야 한다.
    - 즉, 선분 AB의 양 끝점 A, B가 선분 CD를 기준으로 서로 다른 방향에 존재해야 한다.
    - 이를 위해 CCW(Counter Clock Wise)를 사용한다.
    - ccw(A, B, C) * ccw(A, B, D) < 0 이면 교차점이 생긴다.
    - ccw(C, D, A) * ccw(C, D, B) < 0 이면 교차점이 생긴다.

- 일직선상에 존재하여 겹치는 경우
    - ccw(A, B, C) * ccw(A, B, D) == 0 이면 일직선상에 존재한다.
    - ccw(C, D, A) * ccw(C, D, B) == 0 이면 일직선상에 존재한다.
    - 이 때, 선분 AB의 양 끝점 A, B가 선분 CD에 포함되어 있는지 확인해야 한다.
    - 한 선분의 min값이 다른 선분의 max값보다 크거나 같을 때 겹친다.
"""


def ccw(p1, p2, p3):  # p1, p2, p3 : (x, y)
    result = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])

    if result > 0:  # 반시계 방향
        return 1
    elif result < 0:  # 시계 방향
        return -1
    return 0


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


import sys

read = sys.stdin.readline

ax, ay, bx, by = map(int, read().split())
cx, cy, dx, dy = map(int, read().split())

print(1) if is_cross((ax, ay), (bx, by), (cx, cy), (dx, dy)) else print(0)
