# https://www.acmicpc.net/problem/11660

"""
- 처음에 sums = [[0] * (n+1)] * (n+1) 이렇게 했는데, list가 공유되어서 모든 리스트가 같은 값이 나왔다.

- sums를 할 때 n+1 크기로 만든 이유는, 0번째 행과 0번째 열을 0으로 채우기 위해서이다. -> index out of range 방지
- sums에서 n을 사용할 수도 있지만, 이렇게 하면 if문을 사용해 i=0 이거나 j=0인 경우를 따로 처리해야 한다. (총 4가지 경우)
"""

import sys

read = sys.stdin.readline

n, m = map(int, read().split())
numbers = [list(map(int, read().split())) for _ in range(n)]

# sums = [[0] * (n+1)] * (n+1) 이렇게 하면 list가 공유되어서 모든 리스트가 같은 값이 나옴 (같은 주소)
sums = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + numbers[i-1][j-1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, read().split())
    print(sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1])