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


def solution1(s):
    cnt = 0

    for i in range(len(s)):
        if is_valid_bracket(s[i:] + s[:i]):  # 문자열 회전 - 슬라이싱과 연결 연산의 시간 복잡도는 O(n)
            cnt += 1

    return cnt


def solution2(s):
    n = len(s)
    pairs = {']': '[', '}': '{', ')': '('}
    cnt = 0

    for i in range(n):
        stack = []
        is_valid = True

        for j in range(n):
            # 문자열 회전 비용을 줄이기 위해 인덱스로 활용 - 시간 복잡도 O(1)
            bracket = s[(i + j) % n]

            if bracket in pairs:
                if not stack or pairs[bracket] != stack.pop():
                    is_valid = False
                    break
            else:
                stack.append(bracket)

        if is_valid and not stack:
            cnt += 1

    return cnt


print(solution1("[](){}") == 3)
print(solution1("}]()[{") == 2)
