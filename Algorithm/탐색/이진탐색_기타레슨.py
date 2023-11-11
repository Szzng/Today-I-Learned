# https://www.acmicpc.net/problem/2343

import sys

read = sys.stdin.readline

n, m = map(int, read().split())
lessons = list(map(int, read().split()))

start = max(lessons)
end = sum(lessons)

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    total = 0
    for lesson in lessons:
        if total + lesson > mid:
            cnt += 1
            total = 0
        total += lesson

    print(start, mid, end, cnt)

    if cnt <= m:  # 블루레이 개수가 m개 이하일 때 -> 블루레이 크기를 줄여야 함 (블루레이 개수가 적어야 하므로)
        end = mid - 1
    else:  # 블루레이 개수가 m개보다 많을 때 -> 블루레이 크기를 늘려야 함 (블루레이 개수가 많아야 하므로)
        start = mid + 1

# 이거 왜 start이지?????
print(start)
