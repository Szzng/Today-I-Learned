# https://www.acmicpc.net/problem/1915

import sys

read = sys.stdin.readline

n, m = map(int, read().split())
d = [[0] * m for _ in range(n)]  # d[i][j] : (i, j)를 우측 하단 꼭지점으로 하는 정사각형의 최대 변의 길이
max_len = 0

for i in range(n):
    nums = list(read().rstrip())

    for j in range(m):
        d[i][j] = int(nums[j])

        if i > 0 and j > 0 and d[i][j] == 1:
            # (i, j)를 측 하단 꼭지점으로 하는 정사각형의 최대 변의 길이는
            # (i - 1, j), (i, j - 1), (i - 1, j - 1)을 우측 하단 꼭지점으로 하는 정사각형의 최대 변의 길이 중 최소값 + 1
            d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1

        max_len = max(max_len, d[i][j])

print(max_len ** 2)
