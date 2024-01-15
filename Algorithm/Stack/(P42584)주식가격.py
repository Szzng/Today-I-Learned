# https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3


def solution(prices):
    n = len(prices)
    stack = []
    result = [n - 1 - i for i in range(n)]

    for idx, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            top = stack.pop()
            result[top[0]] = idx - top[0]

        stack.append((idx, price))

    return result


print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])
