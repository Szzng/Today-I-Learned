# https://www.acmicpc.net/problem/11758

"""
CCW(Counter Clock Wise) : 반시계 방향
- 세 점 A, B, C가 주어졌을 때, AB 벡터와 BC 벡터의 외적의 방향성을 통해 세 점의 위치관계를 알 수 있다.
- 외적의 방향성이 양수이면 반시계 방향, 음수이면 시계 방향, 0이면 일직선이다.
- (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
"""

import sys

read = sys.stdin.readline

x1, y1 = map(int, read().split())
x2, y2 = map(int, read().split())
x3, y3 = map(int, read().split())

result = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)  # CCW
# result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)


if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)
