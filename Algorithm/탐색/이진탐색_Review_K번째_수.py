# https://www.acmicpc.net/problem/1300

"""
- 단순히 문제만 놓고 본다면 A[N][N]의 배열을 B[N*N]배열에 옮겨놓고 sort함수로 정렬한 뒤 B [K]의 값을 출력하면 되는 문제라고 생각됨
- 그러나 N의 입력이 100,000(십만)까지 가능하며 최악의 경우 N*N이 10^10(백억)이므로 무조건 시간 초과가 발생
- 그리고 A[100001][100001]의 배열 또한 메모리 초과로 사용할 수 없음
- 이분 탐색으로 빠르게 답을 구할 수 있는 알고리즘을 사용해야 함
- end의 초기값은 k : k번째 수는 k보다 클 수 없음
"""

n = int(input())
k = int(input())

start = 1
end = k
ans = 0

while start <= end:
    mid = (start + end) // 2
    count_under_mid = 0

    for i in range(1, n + 1):  # 각 행에서 mid 이하의 수의 개수를 구함
        count_under_mid += min(mid // i, n)  # mid // i는 i행에서 mid 이하의 수의 개수를 의미함

    if count_under_mid >= k:  # mid 이하의 수의 개수가 k개 이상이면
        ans = mid  # 정답 후보로 mid를 저장
        end = mid - 1  # mid를 줄여서 다시 탐색

    else:  # mid 이하의 수의 개수가 k개 미만이면
        start = mid + 1  # mid를 늘려서 다시 탐색

print(ans)
