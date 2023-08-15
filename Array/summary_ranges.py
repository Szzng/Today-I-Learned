# https://leetcode.com/problems/summary-ranges/description/
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]

        start = 0
        result = []
        max_length = len(nums) - 1

        for i in range(0, max_length):
            if nums[i] + 1 != nums[i + 1]:
                result.append([nums[start], nums[i]])
                start = i + 1

            if i + 1 == max_length:
                result.append([nums[start], nums[i + 1]])

        return [f'{start}->{end}' if start != end else f'{start}' for start, end in result]