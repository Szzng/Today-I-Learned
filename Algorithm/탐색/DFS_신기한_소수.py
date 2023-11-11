# https://www.acmicpc.net/problem/2023

"""
- 재귀함수 + 자릿수 개념
- 제일 앞자리를 한 자리 수 소수인 2, 3, 5, 7부터 시작해서 뒤에 자릿수를 하나씩 늘려가며 소수인지 확인
"""


import sys
sys.setrecursionlimit(10000)

n = int(input())


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10, 2):
            if isPrime(num * 10 + i):
                dfs(num * 10 + i)


for i in [2, 3, 5, 7]:
    dfs(i)
