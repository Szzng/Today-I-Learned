"""
# 문제
문자열 리스트 string_list와 쿼리 리스트 query_list가 주어집니다.
각 쿼리 리스트에 있는 문자열이 문자열 리스트에 있는지 여부를 확인해야 합니다.
각 문자열에 대해서 문자열의 존재 여부를 True, False로 표시한 리스트를 반환해야 합니다.

- 문자열의 최대 길이는 10^6
- 해시 충돌은 없다고 가정

# 풀이
- 해시 충돌이 없다는 가정이 있으므로, 해시 테이블을 set으로 구현할 수 있음
('in' 연산은 리스트에서는 O(n) 시간 복잡도를 가지지만, set 또는 dict에서는 O(1) 시간 복잡도를 가짐)

- 중복 계산 방지를 위해 메모이제이션을 사용함
"""


def polynomial_hash(string, base=31, mod=1000000007):
    hash_value = 0

    for char in string:
        hash_value = (hash_value * base + ord(char)) % mod

    return hash_value


def solution(string_list, query_list):
    # 메모이제이션을 위한 딕셔너리
    hash_memo = {}
    # 해시 테이블을 set으로 구현하여 평균 O(1) 시간 복잡도로 조회할 수 있도록 함
    hash_table = set()

    for string in string_list:
        # 이미 계산된 해시 값이 있는지 확인 (메모이제이션)
        if string not in hash_memo:
            hash_memo[string] = polynomial_hash(string)

        hash_table.add(hash_memo[string])

    answer = []
    for query in query_list:
        # 이미 계산된 해시 값이 있는지 확인 (메모이제이션)
        if query not in hash_memo:
            hash_memo[query] = polynomial_hash(query)

        answer.append(hash_memo[query] in hash_table)

    return answer


print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]) == [True, False, False, True])
