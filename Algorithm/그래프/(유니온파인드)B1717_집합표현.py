# https://www.acmicpc.net/problem/1717

"""
# 문제
초기에 n+1개의 집합 {0}, {1}, {2}, ... , {n}이 있다.
여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
집합을 표현하는 프로그램을 작성하시오.

# 입력
첫째 줄에 n, m이 주어진다.
m은 입력으로 주어지는 연산의 개수이다.

다음 m개의 줄에는 각각의 연산이 주어진다.

합집합은 0 a b의 형태로 입력이 주어진다.
이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다.

두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다.
이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.

a, b는 정수이며 a와 b는 같을 수도 있다.

# 출력
1로 시작하는 입력에 대해서 a와 b가 같은 집합에 포함되어 있으면 "YES" 또는 "yes"를,
그렇지 않다면 "NO" 또는 "no"를 한 줄에 하나씩 출력한다.

# 시간제한: 2초
# 시간복잡도:
"""

import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]


def find(x):
    if x == parent[x]:
        return x

    # 루트 노드를 찾아서 갱신하여 경로 압축
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x


def is_same_root(x, y):
    print('YES') if find(x) == find(y) else print('NO')


op_func = {0: union, 1: is_same_root}

for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    op_func[op](a, b)
