# https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3

"""
# 문제
코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.
코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. (동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.)
착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
코니는 하루에 최소 한 개의 의상은 입습니다.

코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.


# 제한사항
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.

# 입력
clothes: [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# 출력: 5

# 시간복잡도:
"""

from collections import Counter


def solution(clothes):
    counter = Counter([kind for clothe, kind in clothes])

    result = 1
    for kind, cnt in counter.items():
        # 해당 종류의 의상을 선택하지 않는 경우인 1을 더해준다.
        result *= (cnt + 1)

    # 모두 안입는 경우는 없으므로 -1
    return result - 1
