# https://www.acmicpc.net/problem/1744

"""
# 그리디 + 우선순위 큐

- 그리디 알고리즘은 현재 상황에서 최선의 선택을 반복하는 알고리즘
- 따라서 우선순위 큐를 사용하여 문제를 해결하는 경우가 흔함
"""

"""
수의 집합을 양수, 음수, 1, 0으로 분류하여 생각하는 것이 핵심
"""

import sys
from queue import PriorityQueue

read = sys.stdin.readline

n = int(read())

positive = PriorityQueue()
negative = PriorityQueue()
ones = 0
zeros = 0

for _ in range(n):
    num = int(read())

    if num > 1:
        positive.put(num * -1)  # 내림차순 정렬을 위하여 -1을 곱해줌
    elif num < 0:
        negative.put(num)
    elif num == 1:
        ones += 1
    else:
        zeros += 1

answer = ones

while positive.qsize() > 1:
    answer += positive.get() * positive.get()

answer += positive.get() * -1 if positive.qsize() else 0  # -1을 곱해준 것을 다시 원래대로 돌려줌

while negative.qsize() > 1:
    answer += negative.get() * negative.get()

answer += negative.get() if negative.qsize() and zeros == 0 else 0

print(answer)
