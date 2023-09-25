# https://www.acmicpc.net/problem/2166


def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])


n = int(input())
x, y = map(int, input().split())  # 기준점

points = [tuple(map(int, input().split())) for _ in range(n - 1)]

answer = 0

for i in range(n - 2):
    answer += ccw((x, y), points[i], points[i + 1])  # 기준점과 선분의 두 점을 이은 선분의 넓이 합

print(round(abs(answer) / 2, 1))
