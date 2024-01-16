# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3


def solution(string):
    stack = []

    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(solution('()()') == True)
print(solution('(())()') == True)
print(solution(')()(') == False)
