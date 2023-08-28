# https://www.acmicpc.net/problem/1850

"""
math 모듈의 gcd 함수도 있음

from math import gcd
a, b = map(int, input().split())
c = gcd(a, b)
print('1' * c)
"""





a, b = map(int, input().split())
if a < b:
    a, b = b, a

while b:
    a, b = b, a % b

print('1' * a)



