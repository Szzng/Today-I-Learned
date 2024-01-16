# https://www.acmicpc.net/problem/2343

"""
# 문제
블루레이에는 총 N개의 강의가 들어가는데, 블루레이를 녹화할 때, "강의의 순서가 바뀌면 안 된다".
즉, i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화해야 한다.
오랜 고민 끝에 강토는 M개의 블루레이에 모든 기타 강의 동영상을 녹화하기로 했다.
이때, 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 단, M개의 블루레이는 모두 "같은 크기"이어야 한다.
강토의 각 강의의 길이가 분 단위(자연수)로 주어진다. 이때, 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 강의의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N)이 주어진다.
다음 줄에는 강토의 기타 강의의 길이가 강의 순서대로 분 단위로(자연수)로 주어진다.
각 강의의 길이는 10,000분을 넘지 않는다.

# 시간제한: 2초
# 시간복잡도: O()
"""
import sys

read = sys.stdin.readline

N, M = map(int, read().split())
lecture_durations = list(map(int, read().split()))

start = max(lecture_durations)
end = sum(lecture_durations)

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    curr_sum = 0

    for duration in lecture_durations:
        if curr_sum + duration > mid:
            cnt += 1
            curr_sum = 0

        curr_sum += duration

    if cnt <= M:  # 블루레이 개수가 M개 이하 -> 블루레이 크기를 더 줄이고 블루레이 개수를 늘려도 됨
        end = mid - 1
    else:  # 블루레이 개수가 M개 초과 -> 블루레이 크기를 더 늘리고 블루레이 개수를 줄여야 함
        start = mid + 1

print(start)