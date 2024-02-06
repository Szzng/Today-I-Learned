# https://www.acmicpc.net/problem/2252

"""
# 문제
N명의 학생들을 키 순서대로 줄을 세우려고 한다.
각 학생의 키를 직접 재서 정렬하면 간단하겠지만,
마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다.
그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.
일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

# 입력
첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다.
M은 키를 비교한 회수이다.

다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다.
이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

학생들의 번호는 1번부터 N번이다.

# 출력
첫째 줄에 학생들을 앞에서부터 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.

# 시간제한: 2초
# 시간복잡도: O()

# 풀이
- 답이 여러가지인 경우 아무거나 출력해도 된다. -> 위상정렬
- 진입차수란 특정한 노드로 들어오는 간선의 개수를 의미한다. (A -> B로 이동하는 간선이 존재한다면, B의 진입차수는 1 증가한다.)
"""
import sys
from collections import deque

read = sys.stdin.readline

num_nodes, num_edges = map(int, read().split())
graph = [[] for _ in range(num_nodes + 1)]
indegree = [0] * (num_nodes + 1)  # 진입차수

for _ in range(num_edges):
    a, b = map(int, read().split())
    graph[a].append(b)
    indegree[b] += 1  # 진입차수 1 증가

q = deque([i for i in range(1, num_nodes + 1) if indegree[i] == 0])  # 진입차수가 0인 노드를 큐에 삽입

while q:
    curr_node = q.popleft()
    print(curr_node, end=' ')

    for next_node in graph[curr_node]:
        indegree[next_node] -= 1  # curr_node와 연결된 간선 제거 (진입차수 1 감소)
        if indegree[next_node] == 0:  # 진입차수가 0이 되면 큐에 삽입
            q.append(next_node)
