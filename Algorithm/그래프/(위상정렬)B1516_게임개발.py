# https://www.acmicpc.net/problem/1516

"""
# 문제
숌 회사에서 이번에 새로운 전략 시뮬레이션 게임 세준 크래프트를 개발하기로 하였다.
핵심적인 부분은 개발이 끝난 상태고, 종족별 균형과 전체 게임 시간 등을 조절하는 부분만 남아 있었다.
게임 플레이에 들어가는 시간은 상황에 따라 다를 수 있기 때문에,
모든 건물을 짓는데 걸리는 최소의 시간을 이용하여 근사하기로 하였다.
물론, 어떤 건물을 짓기 위해서 다른 건물을 먼저 지어야 할 수도 있기 때문에 문제가 단순하지만은 않을 수도 있다.
예를 들면 스타크래프트에서 벙커를 짓기 위해서는 배럭을 먼저 지어야 하기 때문에,
배럭을 먼저 지은 뒤 벙커를 지어야 한다. 여러 개의 건물을 동시에 지을 수 있다.

편의상 자원은 무한히 많이 가지고 있고, 건물을 짓는 명령을 내리기까지는 시간이 걸리지 않는다고 가정하자.

# 입력
첫째 줄에 건물의 종류 수 N(1 ≤ N ≤ 500)이 주어진다.
다음 N개의 줄에는 각 건물을 짓는데 걸리는 시간과 그 건물을 짓기 위해 먼저 지어져야 하는 건물들의 번호가 주어진다.
건물의 번호는 1부터 N까지로 하고, 각 줄은 -1로 끝난다고 하자.
각 건물을 짓는데 걸리는 시간은 100,000보다 작거나 같은 자연수이다.
모든 건물을 짓는 것이 가능한 입력만 주어진다.

# 출력
N개의 각 건물이 완성되기까지 걸리는 최소 시간을 출력한다.

# 시간제한: 2초
# 시간복잡도: O()

# 풀이
어떤 건물을 짓기 위해서 다른 건물을 먼저 지어야 할 수도 있다 -> 위상정렬
여러 개의 건물을 동시에 지을 수 있다. -> 동시에 지어지는 건물들은 순서를 고려하지 않는다.
최소 시간 = 각 건물을 짓는데 걸리는 시간 + 이전 건물을 짓는데 걸리는 시간 중 최대값 (이전 건물이 여러 개일 수 있음)
"""
import sys
from collections import deque

read = sys.stdin.readline

num_nodes = int(read())
graph = [[] for _ in range(num_nodes + 1)]
indegree = [0] * (num_nodes + 1)
time = [0] * (num_nodes + 1)

for i in range(1, num_nodes + 1):
    data = list(map(int, read().split()))
    time[i] = data[0]

    for x in data[1:]:
        if x == -1:
            break
        graph[x].append(i)
        indegree[i] += 1

q = deque([i for i in range(1, num_nodes + 1) if indegree[i] == 0])  # 진입차수가 0인 노드를 큐에 삽입

answer = [0] * (num_nodes + 1)

while q:
    curr_node = q.popleft()
    answer[curr_node] += time[curr_node]  # curr_node의 생산 시간을 더해줌

    for next_node in graph[curr_node]:
        # 현재까지 저장된 값 vs 부모 노드를 생산하는 데 걸리는 시간 중 더 큰 값을 저장
        answer[next_node] = max(answer[next_node], answer[curr_node])

        indegree[next_node] -= 1  # curr_node와 연결된 간선 제거 (진입차수 1 감소)
        if indegree[next_node] == 0:  # 진입차수가 0이 되면 큐에 삽입
            q.append(next_node)

for i in range(1, num_nodes + 1):
    print(answer[i])  # 현재 노드의 최대 시간 + 현재 노드의 생산 시간
