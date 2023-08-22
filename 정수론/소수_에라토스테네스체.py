# https://www.acmicpc.net/problem/1929

m, n = map(int, input().split())
checks = [False, False] + [True] * (n - 1)

for i in range(2, int(n ** 0.5) + 1):
    if checks[i]:
        for j in range(i * 2, n + 1, i):
            checks[j] = False

for i in range(m, n + 1):
    if checks[i]:
        print(i)