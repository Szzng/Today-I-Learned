# https://www.acmicpc.net/problem/10868

import math
import sys

read = sys.stdin.readline

n, m = map(int, read().split())
tree_height = math.ceil(math.log2(n)) + 1
tree_size = 1 << tree_height  # 2 ** tree_height (bit shift 연산 이용_1의 오른쪽에 tree_height개의 0이 채워짐)

tree = [0] * tree_size  # 세그먼트 트리 생성
left = tree_size // 2  # 리프 노드의 시작 인덱스

for i in range(left, left + n):
    tree[i] = int(read())

# init tree
for idx in range(left - 1, 0, -1):
    tree[idx] = min(tree[idx * 2], tree[idx * 2 + 1])


def query(start, end):
    start += left - 1  # 리프 노드의 인덱스로 변환
    end += left - 1

    result = sys.maxsize

    while start <= end:  # start가 end보다 커지면 종료
        if start % 2 == 1:  # 홀수인 경우 -> 오른쪽 자식 노드
            result = min(result, tree[start])  # 노드 값 저장 (질의 범위에 포함되는 노드)
            start += 1  # 본래 부모 노드는 질의 범위에 포함되지 않으므로, 부모 노드를 한 칸 뒤로 이동하기 위해 +1

        if end % 2 == 0:  # 짝수인 경우 -> 왼쪽 자식 노드
            result = min(result, tree[end])  # 노드 값 저장 (질의 범위에 포함되는 노드)
            end -= 1  # 본래 부모 노드는 질의 범위에 포함되지 않으므로, 부모 노드를 한 칸 앞으로 이동하기 위해 -1

        start //= 2  # 부모 노드로 이동
        end //= 2  # 부모 노드로 이동

    return result


for _ in range(m):
    a, b = map(int, read().split())
    print(query(a, b))
