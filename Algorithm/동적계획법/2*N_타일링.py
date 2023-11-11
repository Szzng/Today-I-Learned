# https://www.acmicpc.net/problem/11726

n = int(input())  # 1 <= n <= 1000, 2*n 크기의 직사각형을 1*2, 2*1 타일로 채우는 방법의 수
mod = 10007  # 10007로 나눈 나머지 출력

# 초기화
d = [0] * (n + 1)  # d[i] = 2*i 크기의 직사각형을 채우는 방법의 수
d[1] = 1
if n >= 2:
    d[2] = 2

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2]) % mod

print(d[n])
