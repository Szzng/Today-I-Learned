# https://www.acmicpc.net/problem/11659


"""
input()을 사용하면 시간초과가 나는데,
sys.stdin.readline()을 사용하면 시간초과가 나지 않는다.

IO 문제 - 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있음.
관련 문제: https://www.acmicpc.net/problem/15552
"""

import sys

# read = sys.stdin.readline 로 하고 read().split()
read = lambda: sys.stdin.readline().split()
n, m = map(int, read())
numbers = list(map(int, read()))
sums = [numbers[0]] + [0] * (n-1) # 0번째 인덱스는 자신이 곧 누적합이다.

for i in range(1, n):
    sums[i] = sums[i - 1] + numbers[i]

for _ in range(m):
    i, j = map(int, read())
    print(sums[j - 1] - sums[i - 2] if i >= 2 else sums[j - 1])
