# https://school.programmers.co.kr/learn/courses/30/lessons/12973?language=python3

def solution(string):
    stack = []

    for s in string:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)

    return int(len(stack) == 0)


print(solution("baabaa") == 1)
print(solution("cdcd") == 0)
