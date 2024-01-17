# https://school.programmers.co.kr/learn/courses/30/lessons/159994?language=python3

from collections import deque


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:
        target = goal.popleft()

        if cards1 and cards1[0] == target:
            cards1.popleft()
        elif cards2 and cards2[0] == target:
            cards2.popleft()
        else:
            return 'No'

    return 'Yes'


print(solution(["i", "drink", "water"], ["water", "i", "drink"], ["i", "drink", "water"]) == 'Yes')
print(solution(["i", "drink", "water"], ["water", "i", "drink"], ["water", "water"]) == 'No')
