# https://www.acmicpc.net/problem/11689

"""
자연수 n이 주어졌을 때, GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 구하는 프로그램을 작성하시오.
"""

"""
- n의 서로소를 구하는 문제
- n의 소인수를 구하고, n의 소인수로 나누어 떨어지는 (= 해당 소인수를 공약수로 갖는) k의 개수를 빼주면 됨
"""

"""
오일러 피 : n의 서로소의 개수를 구하는 함수
1. 구하고자 하는 오일러 피의 범위만큼 리스트를 자기 자신의 인덱스값으로 초기화
2. 2부터 시작해 현재 리스트의 값과 인덱스가 같으면 (=소수일 때) 현재 선택된 숫자의 배수에 해당하는 수를 리스트에 끝까지 탐색하며 P[i] = P[i]  - P[i] // i
"""

n = int(input())
result = n

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:  # i가 n의 소인수인 경우
        result -= result // i  # n의 소인수로 나누어 떨어지는 k의 개수를 빼줌

        while n % i == 0:  # i가 n의 소인수가 아닐 때까지 나누어줌
            n //= i

if n > 1:  # 마지막에 남은 소인수가 1이 아니고 1보다 큰 어떤 수인 경우
    result -= result // n

print(result)
