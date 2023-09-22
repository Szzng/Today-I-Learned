# https://www.acmicpc.net/problem/9252

import sys

read = sys.stdin.readline

s1 = ' ' + read().rstrip()
s2 = ' ' + read().rstrip()

d = [[(0, '')] * len(s2) for i in range(len(s1))]  # d[i][j] : s1[:i]와 s2[:j]의 LCS의 길이

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            d[i][j] = (d[i - 1][j - 1][0] + 1, d[i - 1][j - 1][1] + s1[i])
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1], key=lambda x: x[0])

print(d[-1][-1][0])
if d[-1][-1][0] != 0:
    print(d[-1][-1][1])
