# https://www.acmicpc.net/problem/2164

"""
시간 복잡도
- 파이썬 프로그램에서는 1초에 2천만 번 ~ 1억 번의 연산 수행 가능
- 1 ≤ N ≤ 500,000 / 2초
- N이 500,000이므로 1초 안에 해결 가능
"""

from collections import deque

n = int(input())
dq = deque([i for i in range(1, n + 1)])

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])