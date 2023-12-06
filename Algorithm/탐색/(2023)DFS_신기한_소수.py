# https://www.acmicpc.net/problem/2023

"""
- 재귀함수 + 자릿수 개념
- 제일 앞자리를 한 자리 수 소수인 2, 3, 5, 7부터 시작해서 뒤에 자릿수를 하나씩 늘려가며 소수인지 확인
"""


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_prime_numbers(prefix, length):
    if len(str(prefix)) == length:
        print(prefix)
        return

    for digit in range(1, 10, 2):
        new_number = prefix * 10 + digit
        if is_prime(new_number):
            generate_prime_numbers(new_number, length)


def main():
    import sys

    sys.setrecursionlimit(10000)

    n = int(input())

    for num in [2, 3, 5, 7]:
        generate_prime_numbers(num, n)


if __name__ == "__main__":
    main()
