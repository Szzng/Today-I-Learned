# https://www.acmicpc.net/problem/1300

"""
# 문제
크기가 N×N인 배열 A를 만들었다.
배열에 들어있는 수 A[i][j] = i×j 이다.
이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다.
B를 오름차순 정렬했을 때, B[k]를 구해보자.
배열 A와 B의 인덱스는 1부터 시작한다.

# 입력
첫째 줄에 배열의 크기 N이 주어진다. N은 10^5보다 작거나 같은 자연수이다.
둘째 줄에 k가 주어진다. k는 min(10^9, N^2)보다 작거나 같은 자연수이다.

# 시간제한: 2초
# 시간복잡도: O()
- 단순히 문제만 놓고 본다면 A[N][N]의 배열을 B[N*N]배열에 옮겨놓고 sort함수로 정렬한 뒤 B [K]의 값을 출력하면 되는 문제라고 생각됨
- 그러나 N의 입력이 10^5까지 가능하며 최악의 경우 N*N이 10^10이므로 무조건 시간 초과가 발생
- 그리고 A[100001][100001]의 배열 또한 메모리 초과로 사용할 수 없음

# 풀이
- 작은 수의 개수를 세는 것이 핵심
- 이진탐색으로 중앙값보다 작은 수의 개수를 세면서 범위를 절반씩 줄이는 방법
"""

N, k = int(input()), int(input())

start, end = 1, k
answer = 0

while start <= end:
    mid = (start + end) // 2
    count_under_mid = 0

    # 각 행별로 mid 이하의 수의 개수를 세어 count에 더함
    for i in range(1, N + 1):
        # "mid // i"는 i행(i의 곱셈값들)에서 mid 이하의 수의 개수를 의미함
        count_under_mid += min(mid // i, N)

    # count_under_mid == k 더라도, 행렬(곱셈표)에 mid 값이 존재하지 않을 수도 있기 때문에 끝까지 탐색해야 함.
    if count_under_mid >= k:  # mid 이하의 수의 개수가 k개 이상이면
        answer = mid  # 정답 후보로 mid를 저장
        end = mid - 1  # mid를 줄여서 다시 탐색

    else:  # mid 이하의 수의 개수가 k개 미만이면
        start = mid + 1  # mid를 늘려서 다시 탐색

print(answer)
