# https://school.programmers.co.kr/learn/courses/30/lessons/159993?language=python3

"""
# 문제
1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하려고 합니다.
각 칸은 통로 또는 벽으로 구성되어 있으며, 벽으로 된 칸은 지나갈 수 없고 통로로 된 칸으로만 이동할 수 있습니다.
통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있습니다.
레버 또한 통로들 중 한 칸에 있습니다.
따라서, 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다.
이때 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있습니다.
미로에서 한 칸을 이동하는데 1초가 걸린다고 할 때, 최대한 빠르게 미로를 빠져나가는데 걸리는 시간을 구하려 합니다.

미로를 나타낸 문자열 배열 maps가 매개변수로 주어질 때,
미로를 탈출하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요.
만약, 탈출할 수 없다면 -1을 return 해주세요.

# 제한사항
5 ≤ maps의 길이 ≤ 100
5 ≤ maps[i]의 길이 ≤ 100
maps[i]는 다음 5개의 문자들로만 이루어져 있습니다.
S : 시작 지점
E : 출구
L : 레버
O : 통로
X : 벽
시작 지점과 출구, 레버는 항상 다른 곳에 존재하며 한 개씩만 존재합니다.
출구는 레버가 당겨지지 않아도 지나갈 수 있으며, 모든 통로, 출구, 레버, 시작점은 여러 번 지나갈 수 있습니다.

# 입력
maps: ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"] -> 16
maps: ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]	 -> -1

# 시간복잡도:
"""
#
#


from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    q = deque()
    endy = endx = -1

    # 시작점과 출구 좌표 초기화
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                q.append((i, j, 0, 0))  # (y좌표, x좌표, 레버 사용 여부, 시간)
                visited[i][j][0] = True
            elif maps[i][j] == 'E':
                endy, endx = i, j

    while q:
        y, x, lever_used, time = q.popleft()

        if (y, x) == (endy, endx) and lever_used:
            return time

        # 방향을 나타내는 전역 변수
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in DIRECTIONS:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx][lever_used] and maps[ny][nx] != 'X':
                new_lever_used = 1 if maps[ny][nx] == 'L' else lever_used
                q.append((ny, nx, new_lever_used, time + 1))
                visited[ny][nx][new_lever_used] = True

    return -1


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]) == 16)
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]) == -1)
