# https://school.programmers.co.kr/learn/courses/30/lessons/42861?language=python3

"""
# 문제
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때,
최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다.
예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

# 제한사항
- 섬의 개수 n은 1 이상 100 이하입니다.
- costs의 길이는 ((n-1) * n) / 2이하입니다.
- 임의의 i에 대해, costs[i][0] 와 costs[i][1]에는 다리가 연결되는 두 섬의 번호가 들어있고,
  costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
- 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다.
  즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
- 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
- 연결할 수 없는 섬은 주어지지 않습니다.

# 입출력 예
n	costs	                                    return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4

# 시간복잡도:
"""


def solution(n, costs):
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])  # 비용 기준으로 오름차순 정렬

    def find(x):
        if x == parent[x]:
            return x

        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x != y:
            parent[y] = x

    used_edges = 0
    total_weight = 0

    for node1, node2, cost in costs:
        if used_edges == n - 1:
            break

        if find(node1) != find(node2):
            union(node1, node2)
            total_weight += cost
            used_edges += 1

    return total_weight


assert solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4
