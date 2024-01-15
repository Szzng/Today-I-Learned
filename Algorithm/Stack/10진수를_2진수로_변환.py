"""
10진수를 2진수로 변환하기
- 10진수를 2진수로 변환하는 방법은 10진수를 2로 나눈 나머지를 역순으로 나열하면 됨
"""

def solution(decimal):
    stack = []

    while decimal > 0:
        stack.append(decimal % 2)
        decimal //= 2

    return int(''.join(map(str, stack[::-1])))


print(solution(10) == 1010)
print(solution(2) == 10)
