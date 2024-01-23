# https://www.acmicpc.net/problem/10868

"""
# 문제
N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때,
a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수를 찾는 것은 어려운 일이 아니다.
하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다.

여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다.
예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최솟값을 찾아야 한다.
각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.

# 입력
첫째 줄에 N, M이 주어진다.
다음 N개의 줄에는 N개의 정수가 주어진다.
다음 M개의 줄에는 a, b의 쌍이 주어진다.

# 출력
M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 출력한다.

# 시간제한: 1초
# 시간복잡도:
"""

import sys
from math import ceil, log2


class MinSegmentTree:
    def __init__(self, num_leaves):
        self.num_leaves = num_leaves
        self.tree_height = ceil(log2(self.num_leaves)) + 1
        self.tree_size = 1 << self.tree_height

        self.tree = [0] * self.tree_size
        self.idx_first_leaf = self.tree_size // 2

        for idx in range(self.idx_first_leaf, self.idx_first_leaf + self.num_leaves):
            self.tree[idx] = int(sys.stdin.readline())

        for idx in range(self.idx_first_leaf - 1, 0, -1):
            self.tree[idx] = min(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def query(self, start, end):
        start += self.idx_first_leaf - 1
        end += self.idx_first_leaf - 1

        result = sys.maxsize

        while start <= end:
            if start % 2 == 1:
                result = min(self.tree[start], result)
                start += 1

            if end % 2 == 0:
                result = min(self.tree[end], result)
                end -= 1

            start //= 2
            end //= 2

        return result


N, M = map(int, sys.stdin.readline().split())

segment_tree = MinSegmentTree(N)

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(segment_tree.query(start, end))
