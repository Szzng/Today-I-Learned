# https://www.acmicpc.net/problem/2193

n = int(input())  # 1 <= n <= 90, n자리 이친수의 개수

# 초기화
d = [[0, 0] for _ in range(n + 1)]  # d[i][j] : i자리 이친수 중 j로 끝나는 이친수의 개수
d[1] = [0, 1]

for i in range(2, n + 1):
    d[i][0] = d[i - 1][0] + d[i - 1][1]
    d[i][1] = d[i - 1][0]

print(sum(d[n]))
