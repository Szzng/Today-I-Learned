# https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3

"""
# 문제

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
- phone_book의 길이는 1 이상 1,000,000 이하입니다.
- 각 전화번호의 길이는 1 이상 20 이하입니다.
- 같은 전화번호가 중복해서 들어있지 않습니다.

# 입출력 예제
phone_book	                                        return
[119, 97674223, 1195524421]	                        false
[123,456,789]	                                    true
[12,123,1235,567,88]	                            false

# 시간복잡도:
"""


def solution1(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True


def solution2(phone_book):
    hashmap = set(phone_book)

    for phone_number in phone_book:
        temp = ""
        for num in phone_number:
            temp += num
            if temp in hashmap and temp != phone_number:
                return False
    return True
