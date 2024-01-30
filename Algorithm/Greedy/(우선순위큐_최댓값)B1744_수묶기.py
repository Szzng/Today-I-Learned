# https://www.acmicpc.net/problem/1744

"""
# 그리디 + 우선순위 큐
그리디 알고리즘은 현재 상황에서 최선의 선택을 반복하는 알고리즘
따라서 우선순위 큐를 사용하여 문제를 해결하는 경우가 흔함

# 문제
길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다.
하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다.
어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다.
하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다.
그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.

예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다.
하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.

수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.

# 입력
첫째 줄에 수열의 크기 N이 주어진다. N은 50보다 작은 자연수이다.
둘째 줄부터 N개의 줄에 수열의 각 수가 주어진다.
수열의 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

# 시간제한: 2초
# 시간복잡도: O()

# 풀이
- 수의 집합을 <양수, 음수, 1, 0>으로 분류하여 생각하는 것이 핵심
- 1을 따로 카운트하는 것을 자꾸 까먹는데, 1은 곱하지 않고 (곱해봤자 영향이 없으니까) 더하는 것이 좋음
"""

import sys
from queue import PriorityQueue

read = sys.stdin.readline

N = int(read())

negatives = PriorityQueue()
positives = PriorityQueue()
ones = 0  # 1은 곱하지 않고 더하는 것이 이득
zeros = 0  # 나중에 남는 음수에 곱해서 0으로 만드는 데 사용

for _ in range(N):
    num = int(read())

    if num == 1:
        ones += 1
    elif num == 0:
        zeros += 1
    elif num > 1:
        positives.put(-num)  # 내림차순 정렬을 위하여 -1을 곱해줌
    else:  # num < 0
        negatives.put(num)

total = ones
while positives.qsize() > 1:
    total += positives.get() * positives.get()

total += -positives.get() if not positives.empty() else 0  # -1을 곱해준 것을 다시 원래대로 돌려줌

while negatives.qsize() > 1:
    total += negatives.get() * negatives.get()

total += negatives.get() if not negatives.empty() and zeros == 0 else 0

print(total)
