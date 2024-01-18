# https://www.acmicpc.net/problem/1715





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
