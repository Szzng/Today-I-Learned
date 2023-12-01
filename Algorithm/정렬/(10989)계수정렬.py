# https://www.acmicpc.net/problem/10989

"""
# 계수정렬 (Counting Sort)
- 데이터의 값을 직접 비교하지 않고, 데이터의 개수를 세는 알고리즘
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
- 시간복잡도 O(n+k) (n: 데이터의 개수, k: 데이터 중 최대값의 크기)
- 공간복잡도 O(k) (추가적인 메모리(카운트 배열) 필요)
- 작은 범위의 정수에서 다른 정렬 알고리즘보다 빠르고 효율적
- 값의 범위가 크면 적합하지 않을 수 있음 (메모리 제한)

# 문제 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 해결 방법
- 이 문제는 N이 최대 10,000,000이므로, O(NlogN)보다 빠른 정렬 알고리즘을 사용해야 한다.
- 수가 10,000보다 작거나 같은 자연수이므로, 계수정렬을 사용할 수 있다.
"""

import sys
read = sys.stdin.readline

n = int(read())
max_num = 10000 + 1 # 수의 범위가 10000까지이므로 10001개의 배열을 생성
counts = [0] * max_num

for _ in range(n):
    counts[int(read())] += 1 # 입력받은 수를 인덱스로 하여 해당 인덱스의 값을 1 증가

for i in range(max_num):
    for _ in range(counts[i]):
        print(i)
