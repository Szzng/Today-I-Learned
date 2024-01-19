# https://school.programmers.co.kr/learn/courses/30/lessons/72411?language=python3

"""
# 문제


# 입력

# 시간제한: 초
# 시간복잡도:
"""

from itertools import combinations


def solution(orders, course):
    answer = []
    return answer


def solution2(orders, course):
    sort = [sorted(o) for o in orders]
    result = []

    for num in course:
        cnt = {}
        for s in sort:
            for c in list(combinations(s, num)):
                string = ''.join(c)
                cnt[string] = cnt[string] + 1 if string in cnt else 1

        maximum = {}
        for key, value in cnt.items():
            if value > 1 and value in maximum:
                maximum[value].append(key)
            elif value > 1:
                maximum[value] = [key]
        if list(maximum.keys()):
            result += maximum[max(list(maximum.keys()))]
    result.sort()

    return result
