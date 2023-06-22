# https://leetcode.com/problems/house-robber-ii/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        return max(self.get_result(nums[:-1]), self.get_result(nums[1:]))

    def get_result(self, nums_array):
        result = [0, 0]

        while nums_array:
            num = nums_array.pop()
            result = [num + result[1], max(result)]

        return max(result)
