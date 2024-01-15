# https://school.programmers.co.kr/learn/courses/30/lessons/76502?language=python3


def is_valid_bracket(string):
    stack = []
    pairs = {']': '[', '}': '{', ')': '('}

    for s in string:
        if s in pairs:
            if not stack or pairs[s] != stack.pop():
                return False
        else:
            stack.append(s)

    return len(stack) == 0


def solution(s):
    cnt = 0

    for i in range(len(s)):
        if is_valid_bracket(s[i:] + s[:i]):
            cnt += 1

    return cnt
