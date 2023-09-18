# https://www.acmicpc.net/problem/11050

"""
이항계수 : n개의 원소 중에서 k개의 원소를 순서 없이 선택하는 경우의 수
"""

n, k = map(int, input().split())
d = [[0] * (n + 1) for _ in range(n + 1)]  # d[n][k] : n개에서 k개를 선택하는 경우의 수

# 초기화
for i in range(n + 1):
    d[i][0] = 1  # i개에서 1개도 선택하지 않는 경우의 수는 1
    d[i][i] = 1  # i개에서 i개를 선택하는 경우의 수는 1
    d[i][1] = i  # i개에서 1개를 선택하는 경우의 수는 i

# 점화식 : d[n][k] = d[n-1][k-1] + d[n-1][k] (nCk = n-1Ck-1 + n-1Ck)
for i in range(2, n + 1): # 2개부터 n개까지 -> 1개는 초기화에서 이미 계산했음
    for j in range(2, i):  # i개에서 1개 ~ i-1개를 선택하는 경우의 수
        d[i][j] = d[i - 1][j - 1] + d[i - 1][j]

print(d[n][k])
