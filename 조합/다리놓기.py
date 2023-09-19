# https://www.acmicpc.net/problem/1010

import sys

read = sys.stdin.readline
max_num = 30
d = [[0] * max_num for _ in range(max_num)]

# 초기화
for i in range(max_num):
    d[i][0] = 1
    d[i][i] = 1
    d[i][1] = i

for i in range(2, max_num):
    for j in range(2, i):
        d[i][j] = d[i - 1][j - 1] + d[i - 1][j]

T = int(read())

for _ in range(T):
    n, m = map(int, read().split())
    print(d[m][n])
