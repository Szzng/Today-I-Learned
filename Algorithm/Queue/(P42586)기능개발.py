# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3

import math
from collections import deque


def solution1(progresses, speeds):
    Q = []

    for p, s in zip(progresses, speeds):
        day_left = -((p - 100) // s) # 올림: '//' 연산자가 내림 나눗셈을 수행하므로, 음수에 대해서는 올림처럼 수행하게 됨.

        if Q and Q[-1][0] >= day_left:
            Q[-1][1] += 1
        else:
            Q.append([day_left, 1])

    return [q[1] for q in Q]


def solution2(progresses, speeds):
    dq = deque([math.ceil((100 - progress) / speeds[i]) for i, progress in enumerate(progresses)])
    result = []

    while dq:
        front = dq.popleft()
        release_cnt = 1

        while dq and dq[0] <= front:
            dq.popleft()
            release_cnt += 1

        result.append(release_cnt)

    return result
