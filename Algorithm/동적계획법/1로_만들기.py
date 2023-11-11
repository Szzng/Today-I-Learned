# https://www.acmicpc.net/problem/1463

n = int(input())

d = [0, 0, 1, 1] + [0] * (n - 3)

for i in range(4, n + 1):
    d[i] = d[i - 1] + 1  # 1을 빼는 경우

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1) # 2로 나누는 경우

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1) # 3으로 나누는 경우

print(d[n])
