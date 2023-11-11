# https://www.acmicpc.net/problem/1934

"""
유클리드 호제법
- 두 수의 최대공약수를 구하는 알고리즘
- 두 수 a, b에 대해 a를 b로 나눈 나머지를 r이라고 하면, a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
- 나머지 연산을 재귀적으로 반복하면, 나머지가 0이 될 때의 b가 최대공약수이다.
- 시간복잡도: O(logn)
- 최소공배수 = 두 수의 곱 / 최대공약수
"""

import sys

read = sys.stdin.readline


def solution1():
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    t = int(read())
    for _ in range(t):
        a, b = map(int, read().split())
        print(a * b // gcd(a, b))


def solution2():
    t = int(read())
    for _ in range(t):
        a, b = map(int, read().split())

        x, y = a, b
        while y:
            x, y = y, x % y

        print(a * b // x)
