# https://www.acmicpc.net/problem/1043

"""
# 문제
파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다.
지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다.
당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다.
하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다.
문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다.
따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다.
당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다.
지민이는 이런 일을 모두 피해야 한다.

사람의 수 N이 주어진다.
그리고 그 이야기의 진실을 아는 사람이 주어진다.
그리고 각 파티에 오는 사람들의 번호가 주어진다.

지민이는 모든 파티에 참가해야 한다.
이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.

둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다.
진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다.
사람들의 번호는 1부터 N까지의 수로 주어진다.

셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.

N, M은 50 이하의 자연수이고,
진실을 아는 사람의 수는 0 이상 50 이하의 정수,
각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.

# 출력
첫째 줄에 문제의 정답을 출력한다.

# 시간제한: 2초
# 시간복잡도:
"""

import sys

sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x


num_people, num_parties = map(int, read().split())
truth_people = list(map(int, read().split()))
num_truth_people = truth_people.pop(0)

parent = [i for i in range(num_people + 1)]
roots_parties = []

for _ in range(num_parties):
    partiers = list(map(int, read().split()))
    num_partiers = partiers.pop(0)

    if num_partiers == 0:
        continue

    first_partier = partiers[0]
    roots_parties.append(first_partier)
    for i in range(1, num_partiers):
        union(first_partier, partiers[i])

num_truth_party = 0
for root_party in roots_parties:
    for truth_person in truth_people:  # 각 파티의 root와 진실을 아는 사람들의 root가 같으면 (=진실을 아는 사람이 파티에 있음)
        if find(root_party) == find(truth_person):
            num_truth_party += 1
            break

print(num_parties - num_truth_party)
