# https://school.programmers.co.kr/learn/courses/30/lessons/120853?language=python3

def solution(s):
    nums = s.split()
    stack = []

    for num in nums:
        if num == 'Z' and stack:
            stack.pop()
        else:
            stack.append(int(num))

    return sum(stack)


print(solution("1 2 Z 3") == 4)
print(solution("-1 -2 -3 Z") == -3)
