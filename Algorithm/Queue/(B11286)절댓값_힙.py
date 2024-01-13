# https://www.acmicpc.net/problem/11286

"""
- 시간복잡도 : N(1≤N≤100,000), 1초 -> O(NlogN) 이내로 해결 필요
- sys.stdin.readline, sys.stdout.write 이용하지 않고 input, print 이용 시 시간초과
"""

import sys
from queue import PriorityQueue

read = sys.stdin.readline
write = sys.stdout.write
pq = PriorityQueue()

n = int(read())

for i in range(n):
    x = int(read())
    if x != 0:
        # 우선순위 큐의 정렬 기준 설정하여 데이터 추가
        # 절댓값을 기준으로 정렬하고, 같으면 음수를 우선 정렬하도록 구성
        pq.put((abs(x), x))

    else:
        if pq.empty():
            write('0\n')
        else:
            write(f'{pq.get()[1]}\n')
