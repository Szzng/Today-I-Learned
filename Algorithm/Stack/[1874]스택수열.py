# https://www.acmicpc.net/problem/1874

"""
- sys.stdin.readline()을 사용하면 확실히 훨씬 빠르다.
"""
import sys

read = sys.stdin.readline

# solution1
n = int(read())
stack = []
result = []
curr_num = 1

for i in range(n):
    target = int(read())

    while curr_num <= target:
        stack.append(curr_num)
        curr_num += 1
        result.append('+')

    if stack[-1] == target:
        stack.pop()
        result.append('-')

    else:
        print('NO')
        sys.exit()

print(*result, sep='\n')

# solution2
n = int(read())
nums = [int(read()) for _ in range(n)]
stack = []
result = []

for i in range(1, n + 1):
    if i <= nums[0]:
        stack.append(i)
        result.append('+')

    while nums and stack and nums[0] == stack[-1]:
        stack.pop() # O(1)
        nums.pop(0)  # O(n) : shifting all elements after the popped element (inefficient)
        result.append('-')

while stack:
    result.append('-')
    if stack.pop() != nums.pop(0):
        result = ['NO']
        break

print(*result, sep='\n')
