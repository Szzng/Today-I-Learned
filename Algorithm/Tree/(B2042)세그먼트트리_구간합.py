# https://www.acmicpc.net/problem/2042


"""
# 문제
어떤 N개의 수가 주어져 있다.
그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다.
만약에 1,2,3,4,5 라는 수가 있고,
3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다.
그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.

# 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과
M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다.
M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다.

그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다.
그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데,
a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고
a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.

입력으로 주어지는 모든 수는 -2^63보다 크거나 같고, 2^63-1보다 작거나 같은 정수이다.

# 출력
첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다.
단, 정답은 -2^63보다 크거나 같고, 2^63-1보다 작거나 같은 정수이다.


# 시간제한: 2초
# 시간복잡도:

# 풀이
- "그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다."  => 세그먼트 트리
- 합 배열은 자료구조의 특성상 데이터 변경에 시간이 오래 걸리지만, 세그먼트 트리는 데이터 변경에 시간이 오래 걸리지 않음
"""

import sys
from math import ceil, log2


class SegmentTree:
    def __init__(self, num_leaves):
        self.num_leaves = num_leaves
        self.tree_height = ceil(log2(num_leaves)) + 1
        self.tree_size = 1 << self.tree_height  # 2 ** tree_height (bit shift 연산 이용_1의 오른쪽에 tree_height개의 0이 채워짐)

        self.tree = [0] * self.tree_size  # 세그먼트 트리 생성
        self.idx_first_leaf = self.tree_size // 2  # 리프 노드의 시작 인덱스 (루트 노드 인덱스는 1)

        for idx in range(self.idx_first_leaf, self.idx_first_leaf + self.num_leaves):
            self.tree[idx] = int(sys.stdin.readline())

        for idx in range(self.idx_first_leaf - 1, 0, -1):  # 리프 노드의 부모 노드부터 시작
            self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]  # 왼쪽 자식 + 오른쪽 자식

    def update(self, index, value):
        index += self.idx_first_leaf - 1  # 인덱스를 리프 노드의 인덱스로 변환
        diff = value - self.tree[index]  # 변경된 값과 기존 값의 차이

        while index > 0:
            self.tree[index] += diff  # 갱신
            index //= 2  # 부모 노드로 이동

    def query(self, start, end):
        start += self.idx_first_leaf - 1
        end += self.idx_first_leaf - 1

        result = 0

        while start <= end:  # start가 end보다 커지면 종료
            if start % 2 == 1:  # 홀수인 경우 -> 오른쪽 자식 노드
                result += self.tree[start]  # 노드 값 저장 (질의 범위에 포함되는 노드)
                start += 1  # 본래 부모 노드는 질의 범위에 포함되지 않으므로, 부모 노드를 한 칸 뒤로 이동하기 위해 +1

            if end % 2 == 0:  # 짝수인 경우 -> 왼쪽 자식 노드
                result += self.tree[end]  # 노드 값 저장 (질의 범위에 포함되는 노드)
                end -= 1  # 본래 부모 노드는 질의 범위에 포함되지 않으므로, 부모 노드를 한 칸 앞으로 이동하기 위해 -1

            start //= 2  # 부모 노드로 이동
            end //= 2  # 부모 노드로 이동

        return result


N, M, K = map(int, sys.stdin.readline().split())

segment_tree = SegmentTree(N)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        segment_tree.update(b, c)
    else:
        print(segment_tree.query(b, c))
