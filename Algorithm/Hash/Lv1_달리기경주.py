# https://school.programmers.co.kr/learn/courses/30/lessons/178871

"""
2개의 딕셔너리를 이용해서 서로 키와 값을 교차해 비교하며 문제를 해결했다.

다른 풀이에서는 딕셔너리를 1개만 사용하는 대신,
각 반복마다 직접 리스트 내 데이터의 위치를 바꾸며 문제를 해결했는데,
이것보다는 딕셔너리로 해결하는 것이 더 효율적이라고 생각했다.
"""


def solution(players, callings):
    by_name, by_order = {}, {}

    for i, player in enumerate(players):
        by_name[player] = i
        by_order[i] = player

    for name in callings:
        front = by_order[by_name[name] - 1]

        by_name[front] += 1
        by_name[name] -= 1

        by_order[by_name[front]] = front
        by_order[by_name[name]] = name

    return list(by_order.values())
