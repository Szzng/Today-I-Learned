# https://www.acmicpc.net/problem/14425

"""
# 문제
총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서
집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.
다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.
입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다.
집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

# 출력
첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

# 시간제한: 2초
# 시간복잡도:
"""

import sys

read = sys.stdin.readline

N, M = map(int, input().split())
hash_table = set([read() for _ in range(N)])
count = 0

for _ in range(M):
    if read() in hash_table:
        count += 1

print(count)
