# https://www.acmicpc.net/problem/14501

n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]

d = [0] * (n + 1)  # d[i] : i번째 날부터 마지막 날까지 낼 수 있는 최대 이익

for i in range(n - 1, -1, -1):
    if tp[i][0] + i > n:  # 상담이 끝나는 날이 퇴사일을 넘어가면
        d[i] = d[i + 1]  # 이익은 다음 날의 이익과 같다
    else:
        d[i] = max(d[i + 1], tp[i][1] + d[tp[i][0] + i])  # 상담을 하는 경우와 하지 않는 경우 중 최대 이익

print(d[0])
