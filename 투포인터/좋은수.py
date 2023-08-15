# https://www.acmicpc.net/problem/1253

"""
만약 좋은 수 하나를 찾는데 시간 복잡도가 n^2이라면, n개의 좋은 수를 찾는데는 n^3이 걸린다. -> 시간 초과
따라서 좋은 수 하나를 찾는 알고리즘의 시간 복잡도는 최소 O(nlogn)이어야 한다. -> 정렬, 투포인터


n개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
-> 처음에 값이 같으면 같은 수라고 생각하고 idx를 비교하는 것이 아니라 num을 비교했으나, 알고 보니 idx가 다르면 다른 수였음.
-> 예를 들면 0 0 0 0 이 주어졌을 때 답은 4임.
"""

import sys
read = sys.stdin.readline

n = int(read())
numbers = sorted(list(map(int, read().split())))
cnt = 0

for idx, num in enumerate(numbers):
    left, right = 0, n - 1

    while left < right:
        if numbers[left] + numbers[right] == num:
            if left != idx and right != idx:
                cnt += 1
                break
            elif left == idx:
                left += 1
            else:
                right -= 1
        elif numbers[left] + numbers[right] < num:
            left += 1
        else:
            right -= 1

print(cnt)