# https://www.acmicpc.net/problem/11051


n, k = map(int, input().split())
mod = 10007  # 문제 조건

d = [[0] * (n + 1) for _ in range(n + 1)]  # d[n][k] : n개에서 k개를 선택하는 경우의 수

# 초기화
for i in range(n + 1):
    d[i][0] = 1
    d[i][i] = 1
    d[i][1] = i

# 점화식 : d[n][k] = d[n-1][k-1] + d[n-1][k] (nCk = n-1Ck-1 + n-1Ck)
for i in range(2, n + 1):
    for j in range(2, i):
        d[i][j] = (d[i - 1][j - 1] + d[i - 1][j]) % mod

print(d[n][k])
