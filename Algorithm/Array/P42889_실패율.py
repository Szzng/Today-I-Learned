# https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3

def solution(N, stages):
    counts = [0] * (N + 2)
    for stage in stages:
        counts[stage] += 1

    players = len(stages)
    fail = {}
    stop_idx = N + 1

    for i in range(1, N + 1):
        fail[i] = counts[i] / players
        players -= counts[i]

        if players == 0:
            stop_idx = i + 1
            break

    # fail의 value를 기준으로 내림차순 정렬 후 key만 반환 + stop_idx부터 N까지의 key 반환
    return sorted(fail, key=lambda x: fail[x], reverse=True) + [i for i in range(stop_idx, N + 1)]