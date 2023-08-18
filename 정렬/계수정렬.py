# https://www.acmicpc.net/problem/10989

"""
계수정렬 (Counting Sort)
- 데이터의 값을 직접 비교하지 않고, 데이터의 개수를 세는 알고리즘
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
- 시간복잡도 O(n+k) (k: 데이터 중 최대값)
- 데이터의 개수가 많을 때는 사용하기 어려움 (메모리 제한)

문제 입력 : 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
- 이 문제는 N이 최대 10,000,000이므로, O(NlogN)보다 빠른 정렬 알고리즘을 사용해야 한다.
- 수가 10,000보다 작거나 같은 자연수이므로, 계수정렬을 사용할 수 있다.
"""

import sys
read = sys.stdin.readline

n = int(read())
max_num = 10000 + 1
counts = [0] * max_num

for _ in range(n):
    counts[int(read())] += 1

for i in range(max_num):
    if counts[i] > 0:
        for _ in range(counts[i]):
            print(i)
