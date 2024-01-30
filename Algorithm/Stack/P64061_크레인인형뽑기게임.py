# https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3


def solution(board, moves):
    stack = []
    result = 0

    for move in moves:
        for lanes in board:
            if lanes[move - 1]:
                stack.append(lanes[move - 1])
                lanes[move - 1] = 0
                break

        if len(stack) > 1 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
            result += 2

    return result


print(solution(
    [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
    [1, 5, 3, 5, 1, 2, 1, 4]) == 4)
