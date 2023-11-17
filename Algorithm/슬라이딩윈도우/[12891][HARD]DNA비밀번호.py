# https://www.acmicpc.net/problem/12891

"""
1. init 문자열을 먼저 정해 검사해놓고, 나가는 문자 1개와 들어오는 문제 1개만 처리하는 것이 핵심!!!
  - 처음에는 계속 target = dna[i:i+p] 이런 식으로 놓고 다시 target 안에서 for문을 돌리는 이중 for문으로 풀었는데 시간 초과가 남.

2. must 딕셔너리를 이용해 cnt 수를 늘리는 조건을 잘못 놔서 계속 틀림
  - 정답. all([v <= 0 for v in must.values()] -> must 딕셔너리의 모든 value가 0 이하일 때가 바로 조건에 만족하는 것!!!

  - 오답1. must[key]를 0 이상을 기준으로만 생각함 -> 음수도 가능하도록 무조건 세어주어야 out과 new의 입출에도 불구하고 전체 문자열에서 해당 key 알파벳이 몇 개인지 정확히 알 수 있음.
  - 오답2. sum(must.values()) == 0 -> 음수와 양수가 존재할 때 서로 더해지며 0이 되는 경우가 있을 수 있음.
"""

import sys

s, p = map(int, input().split())
dna = sys.stdin.readline()
conditions = list(map(int, input().split()))
must = {k: conditions[idx] for idx, k in enumerate('ACGT')}
# A, C, G, T = map(int, read().split())
# must = {'A': A, 'C': C, 'G': G, 'T': T}

cnt = 0

init = dna[:p]
for n in init:
    if n in must:
        must[n] -= 1

if all([v <= 0 for v in must.values()]):
    cnt += 1

for i in range(p, s):
    out = dna[i - p]
    if out in must:
        must[out] += 1

    new = dna[i]
    if new in must:
        must[new] -= 1

    if all([v <= 0 for v in must.values()]):
        cnt += 1

print(cnt)
