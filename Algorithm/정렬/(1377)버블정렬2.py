# https://www.acmicpc.net/problem/1377

"""
# 버블정렬

``` C++
bool changed = false;

for (int i=1; i<=N+1; i++) {
    changed = false;

    for (int j=1; j<=N-i; j++) {
        if (A[j] > A[j+1]) {
            changed = true;
            swap(A[j], A[j+1]);
        }
    }

    if (changed == false) {     // i번째 루프에서 swap이 한 번도 일어나지 않았다면 = 이미 정렬이 완료되었다면
        cout << i << '\n';      // i번째 루프가 마지막 루프이므로 i 출력
        break;                  // 이미 정렬이 완료되었으므로 더 이상의 루프는 불필요
    }
}
```
- 버블정렬의 swap이 한 번도 일어나지 않은 루프가 언제인지 = 이미 모든 데이터가 정렬 완료된 때를 찾는 문제
- 이중 for문에서 안쪽 for문 전체를 돌 때 swap이 한 번도 일어나지 않았다면 이미 정렬이 완료된 것
- 그러나 n의 최대범위가 500,000이므로 버블정렬의 O(n^2)은 시간초과 -> 다른 방법 필요


# 안쪽 for문이 몇 번 수행되었는지 확인하는 방법
- 안쪽 루프는 1에서 n-j까지, 즉 왼쪽에서 오른쪽으로 이동하면서 swap을 한다.
- 이는 특정 데이터가 안쪽 루프에서 swap의 왼쪽으로 이동할 수 있는 최대거리가 1이라는 뜻이다.
- 따라서 데이터 정렬 전 index와 정렬 후 index를 비교해 왼쪽으로 가장 많이 이동한 값을 찾으면 된다.
- 파이썬에서 기본적으로 제공하는 정렬 알고리즘은 O(nlogn)이므로 시간초과가 나지 않음 -> 정렬 후 index를 비교하는 방법으로 해결 가능
"""

import sys
read = sys.stdin.readline

n = int(read())
nums = [(int(read()), i) for i in range(n)] # 정렬 전 index를 저장하기 위해 tuple로 저장
sorted_nums = sorted(nums) # 정렬 후 index를 비교하기 위해 정렬, 파이썬 기본 정렬 알고리즘은 O(nlogn)이므로 시간초과가 나지 않음

maxmove = 0
for j in range(n):
    move = sorted_nums[j][1] - j  # 정렬 전 index - 정렬 후 index(=j)
    if move > maxmove:
        maxmove = move

print(maxmove + 1)  # swap이 한 번도 일어나지 않은 루프가 마지막에 1번 있으므로 1을 더해줌
