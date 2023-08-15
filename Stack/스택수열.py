# https://www.acmicpc.net/problem/1874

"""
- sys.stdin.readline()을 사용하면 확실히 훨씬 빠르다.
- solution1은 내 풀이, solution2는 다른 사람의 풀이인데, 내것이 더 빠르다! 왜인지는 모름.
"""

from sys import stdin
input = stdin.readline

# solution1
n = int(input())
nums = [int(input()) for _ in range(n)]
stack = []
result = []

for i in range(1, n + 1):
    if i <= nums[0]:
        stack.append(i)
        result.append('+')

    while nums and stack and nums[0] == stack[-1]:
        stack.pop()
        nums.pop(0)
        result.append('-')

while stack:
    result.append('-')
    if stack.pop() != nums.pop(0):
        result = ['NO']
        break

print(*result, sep='\n')

# solution2
n = int(input())
numbers = [int(input()) for _ in range(n)]
stack = []
result = ''
num = 1

for i in range(n):
    target = numbers[i]

    while num <= target:
        stack.append(num)
        num += 1
        result += '+\n'

    if stack[-1] == target:
        stack.pop()
        result += '-\n'

    else:
        result = 'NO'
        break

print(result)
