# https://www.acmicpc.net/problem/2018

n = int(input())
cnt = 0
total = 0
start = end = 0

while end <= n:
    if total == n:
        cnt += 1

    if total <= n:
        end += 1
        total += end
    else: # total > n
        total -= start
        start += 1

print(cnt)