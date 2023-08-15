# https://www.acmicpc.net/problem/11003

"""
deque + 슬라이딩 윈도우
정렬 알고리즘을 사용하지 않고도 슬라이딩 윈도우와 덱을 이용해 정렬 효과를 보는 문제
"""

import sys
from collections import deque

read = sys.stdin.readline

n, l = map(int, read().split())
numbers = list(map(int, read().split()))
dq = deque()
result = []

for idx, num in enumerate(numbers):
    while dq and dq[-1][1] > num:  # 덱의 마지막 값이 현재 값보다 크면 제거
        dq.pop()

    dq.append((idx, num))

    if dq[0][0] <= idx - l:  # 범위에서 벗어난 값은 덱에서 제거
        dq.popleft()

    # 덱의 첫 번째 값이 최솟값
    # print(dq[0][1], end=' ')
    result.append(dq[0][1])

print(*result)
