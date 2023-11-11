# https://www.acmicpc.net/problem/1043

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parents[y] = x


truth = list(map(int, input().split()))
del truth[0]

root_party = []
for _ in range(m):
    party = list(map(int, input().split()))
    del party[0]

    if len(party) > 0:
        for i in range(1, len(party)):
            union(party[0], party[i])

        root_party.append(party[0])

result = 0
for i in range(len(root_party)):
    is_possible = True

    for t in truth:
        if find(root_party[i]) == find(t): # 각 파티의 root와 진실을 아는 사람들의 root가 같으면 (=진실을 아는 사람이 파티에 있음)
            is_possible = False
            break

    if is_possible:
        result += 1

print(result)
