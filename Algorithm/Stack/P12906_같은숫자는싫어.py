# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    stack = []

    for num in arr:
        if not stack or stack[-1] != num:
            stack.append(num)

    return stack


print(solution([1, 1, 3, 3, 0, 1, 1]) == [1, 3, 0, 1])
print(solution([4, 4, 4, 3, 3]) == [4, 3])
