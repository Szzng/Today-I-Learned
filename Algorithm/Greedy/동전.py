# https://www.acmicpc.net/problem/11047


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

cnt = 0

for coin in coins:
    if k < coin:
        continue

    cnt += k // coin
    k %= coin

    if k == 0:
        break

print(cnt)
