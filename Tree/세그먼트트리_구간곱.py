# https://www.acmicpc.net/problem/11505

import math
import sys

read = sys.stdin.readline
MOD = 1000000007  # 문제 조건 (MOD로 나눈 나머지 출력)

n, m, k = map(int, read().split())
tree_height = math.ceil(math.log2(n)) + 1
tree_size = 1 << tree_height  # 2 ** tree_height (bit shift 연산 이용_1의 오른쪽에 tree_height개의 0이 채워짐)

tree = [0] * tree_size  # 세그먼트 트리 생성
left = tree_size // 2  # 리프 노드의 시작 인덱스

for i in range(left, left + n):
    tree[i] = int(read())

for idx in range(left - 1, 0, -1):
    tree[idx] = tree[idx * 2] * tree[idx * 2 + 1] % MOD  # 왼쪽 자식 * 오른쪽 자식


def update(index, value):
    index += left - 1  # 리프 노드의 인덱스로 변환
    tree[index] = value  # 변경된 값 저장

    while index > 0:
        index //= 2
        tree[index] = tree[index * 2] * tree[index * 2 + 1] % MOD  # 갱신


def query(start, end):
    start += left - 1  # 리프 노드의 인덱스로 변환
    end += left - 1

    result = 1

    while start <= end:  # start가 end보다 커지면 종료
        if start % 2 == 1:  # 홀수인 경우 -> 오른쪽 자식 노드
            result = result * tree[start] % MOD  # 노드 값 저장 (질의 범위에 포함되는 노드)
            start += 1  # 본래 부모 노드는 질의 범위에 포함되지 않으므로, 부모 노드를 한 칸 뒤로 이동하기 위해 +1

        if end % 2 == 0:  # 짝수인 경우 -> 왼쪽 자식 노드
            result = result * tree[end] % MOD  # 노드 값 저장 (질의 범위에 포함되는 노드)
            end -= 1  # 본래 부모 노드는 질의 범위에 포함되지 않으므로, 부모 노드를 한 칸 앞으로 이동하기 위해 -1

        start //= 2  # 부모 노드로 이동
        end //= 2  # 부모 노드로 이동

    return result


for _ in range(m + k):
    a, b, c = map(int, read().split())

    if a == 1:
        update(b, c)
    else:
        print(query(b, c))
