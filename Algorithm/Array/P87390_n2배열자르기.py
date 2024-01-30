# https://school.programmers.co.kr/learn/courses/30/lessons/87390?language=python3

"""
문제가 복잡하고 어려워보이고, 문제 그대로 구현하면 시간초과가 남.
left와 right 인덱스가 행열에서 뜻하는 바를 알면 몫과 나머지로 쉽게 풀 수 있음.
"""


def solution(n, left, right):
    result = []

    for i in range(left, right + 1):
        result.append(max(i // n, i % n) + 1)

    return result


print(solution(3, 2, 5) == [3, 2, 2, 3])
print(solution(4, 7, 14) == [4, 3, 3, 3, 4, 4, 4, 4])
