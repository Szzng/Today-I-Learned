# https://www.acmicpc.net/problem/2251

"""
# 문제
각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다.
처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다.

이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데,
이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다.
이 과정에서 손실되는 물은 없다고 가정한다.

이와 같은 과정을 거치다보면 세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다.
첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을
모두 구해내는 프로그램을 작성하시오.

# 입력
첫째 줄에 세 정수 A, B, C가 주어진다.

# 출력
첫째 줄에 공백으로 구분하여 답을 출력한다.
각 용량은 오름차순으로 정렬한다.

# 시간제한: 2초
# 시간복잡도: O()

# 풀이
 그래프를 그리는 방식으로 접근하는 문제
- a, b, c의 특정 무게 상태를 1개의 노드로 가정하고, 조건에 따라 이 상태에서 변경할 수 있는 이후 무게 상태가 에지로 이어진 인접한 노드가 됨
- sender, receiver 리스트를 이용하여 6가지 이동 케이스를 정의하고, 이를 이용하여 그래프를 그림
"""
from collections import deque

full = list(map(int, input().split()))
TOTAL = full[-1]
answer = [TOTAL]

start_node = (0, 0)
q = deque([start_node])

visited = set()
visited.add(start_node)

# 6가지 이동 케이스 정의 (0: A, 1: B, 2: C를 나타냄)
cases = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

while q:
    curr_node = q.popleft()

    for sender, receiver in cases:
        next_node = [*curr_node, TOTAL - sum(curr_node)]

        if next_node[sender] == 0 or full[receiver] == next_node[receiver]:
            continue

        next_node[receiver] += next_node[sender]
        next_node[sender] = 0

        if next_node[receiver] > full[receiver]:
            next_node[sender] = next_node[receiver] - full[receiver]
            next_node[receiver] = full[receiver]

        next_node_tuple = (next_node[0], next_node[1])
        if next_node_tuple not in visited:
            visited.add(next_node_tuple)
            q.append(next_node_tuple)

            if next_node[0] == 0:  # a의 무게가 0이면 c의 무게를 answer에 추가
                answer.append(next_node[2])

print(*sorted(answer))
