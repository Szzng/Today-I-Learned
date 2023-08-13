# https://www.acmicpc.net/problem/10986

"""
sums[i]%M == sums[j]%M 이면, (sums[i] - sums[j])%M == 0 이므로, 나머지가  같은 구간의 개수를 구하면 된다.

나머지가 원래 0인 것은 당연히 무조건 포함되므로, answer에 미리 더해준다.
"""


import sys

read = sys.stdin.readline

n, m = map(int, read().split())
numbers = list(map(int, read().split()))
sums = [0] * len(numbers)
answer = 0
remain_dict = {}

for i in range(n):
    sums[i] = sums[i - 1] + numbers[i] if i != 0 else numbers[i]

    remain = sums[i] % m
    if remain == 0:
        answer += 1

    remain_dict[remain] = remain_dict.get(remain, 0) + 1

for value in remain_dict.values():
    answer += value * (value - 1) // 2

print(answer)
