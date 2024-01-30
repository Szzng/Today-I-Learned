# https://www.acmicpc.net/problem/1920

"""
# 문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

# 시간제한: 1초
# 시간복잡도: O(NlogN+MlogN)
"""
import sys

read = sys.stdin.readline

n = int(read())
nums = sorted(list(map(int, read().split())))

m = int(read())
targets = list(map(int, read().split()))

for target in targets:
    left, right = 0, n - 1
    flag = 0

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            flag = 1
            break
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    print(flag)
