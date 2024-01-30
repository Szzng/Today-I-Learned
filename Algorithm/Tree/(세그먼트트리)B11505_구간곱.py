# https://www.acmicpc.net/problem/11505

"""
# 문제
어떤 N개의 수가 주어져 있다.
그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 곱을 구하려 한다.
만약에 1, 2, 3, 4, 5 라는 수가 있고,
3번째 수를 6으로 바꾸고 2번째부터 5번째까지 곱을 구하라고 한다면 240을 출력하면 되는 것이다.
그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 곱을 구하라고 한다면 48이 될 것이다.

# 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다.
M은 수의 변경이 일어나는 횟수이고, K는 구간의 곱을 구하는 횟수이다.
그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다.
그리고 N+2번째 줄부터 N+M+K+1 번째 줄까지 세 개의 정수 a,b,c가 주어지는데,
a가 1인 경우 b번째 수를 c로 바꾸고
a가 2인 경우에는 b부터 c까지의 곱을 구하여 출력하면 된다.

입력으로 주어지는 모든 수는 0보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지를 출력한다.

# 시간제한: 1초
# 시간복잡도:
"""

import sys
from math import ceil, log2


class ProductSegmentTree:
    def __init__(self, num_leaves, MOD):
        self.MOD = MOD
        self.num_leaves = num_leaves
        self.tree_height = ceil(log2(self.num_leaves)) + 1
        self.tree_size = 1 << self.tree_height

        self.tree = [0] * self.tree_size
        self.idx_first_leaf = self.tree_size // 2

        for idx in range(self.idx_first_leaf, self.idx_first_leaf + self.num_leaves):
            self.tree[idx] = int(sys.stdin.readline())

        for idx in range(self.idx_first_leaf - 1, 0, -1):
            self.tree[idx] = self.tree[idx * 2] * self.tree[idx * 2 + 1] % self.MOD

    def update(self, index, value):
        index += self.idx_first_leaf - 1
        self.tree[index] = value

        while index > 0:
            index //= 2
            self.tree[index] = self.tree[index * 2] * self.tree[index * 2 + 1] % self.MOD

    def query(self, start, end):
        start += self.idx_first_leaf - 1
        end += self.idx_first_leaf - 1

        result = 1

        while start <= end:
            if start % 2 == 1:
                result = result * self.tree[start] % self.MOD
                start += 1

            if end % 2 == 0:
                result = result * self.tree[end] % self.MOD
                end -= 1

            start //= 2
            end //= 2

        return result


N, M, K = map(int, sys.stdin.readline().split())

segment_tree = ProductSegmentTree(N, 1000000007)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        segment_tree.update(b, c)
    else:
        print(segment_tree.query(b, c))
