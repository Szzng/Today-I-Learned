# https://www.acmicpc.net/problem/11003

"""
deque + 슬라이딩 윈도우
정렬 알고리즘을 사용하지 않고도 덱과 슬라이딩 윈도우를 이용해 정렬 효과를 보는 문제

deque(덱)
- 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조 (양방향 큐)
- 양끝 삽입/삭제: O(1) -> 리스트에 비해 효율적 (리스트는 pop(0)이 O(n))
- 슬라이싱 불가능
- append, appendleft, pop, popleft, extend, extendleft, remove, rotate 등의 메서드 제공
"""

import sys
from collections import deque

n, l = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))
dq = deque()
result = []

for idx, num in enumerate(nums):

    # 덱의 마지막 값이 현재 값보다 크면 제거하기를 반복 -> 덱의 데이터들은 오름차순으로 정렬됨
    while dq and dq[-1][1] > num:
        dq.pop()

    dq.append((idx, num))

    # 범위에서 벗어난 값은 덱에서 제거
    if dq[0][0] <= idx-l:
        dq.popleft()

    # 덱은 오름차순으로 정렬되어 있으므로 덱의 첫 번째 값이 최솟값
    # print(dq[0][1], end=' ')
    result.append(dq[0][1])

print(*result)
