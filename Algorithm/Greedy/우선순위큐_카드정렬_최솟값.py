# https://www.acmicpc.net/problem/1715

"""
# 그리디 + 우선순위 큐

- 그리디 알고리즘은 현재 상황에서 최선의 선택을 반복하는 알고리즘
- 따라서 우선순위 큐를 사용하여 문제를 해결하는 경우가 흔함
"""

"""
- 처음에는 구간합처럼 for문에서 cards[i] = cards[i-1] + cards[i]를 하고 print(sum(cards[1:]))을 했는데 아래 반례가 생김

- n=4, cards = [20, 30, 40, 45] 일 때, 20과 30을 더해서 50이 된 후 내 코드에서는 50과 40을 더해버리지만, 45와 40을 더해야 맞음 -> 정렬이 흐트러짐

- 즉 더해가는 와중에도 정렬이 항상 유지되어야만 함. 그래서 우선순위 큐를 사용해야 함!
"""

import sys
from queue import PriorityQueue

read = sys.stdin.readline

n = int(read())
pq = PriorityQueue()

for _ in range(n):
    pq.put(int(read()))

answer = 0

while pq.qsize() > 1:
    sums = pq.get() + pq.get()
    answer += sums
    pq.put(sums)

print(answer)
