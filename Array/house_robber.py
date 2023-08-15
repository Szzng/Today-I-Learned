# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    def rob1(self, nums: List[int]) -> int:
        result = [[0, 0]]

        while nums:
            num = nums.pop()
            child = result[-1]
            with_num = num + child[1]
            without_num = max(child)
            result.append([with_num, without_num])

        return max(result[-1])

    def rob2(self, nums: List[int]) -> int:
        result = [[0, 0]]

        def dfs(nums):
            if not len(nums):
                return

            num = nums.pop()
            child = result[-1]
            with_num = num + child[1]
            without_num = max(child)
            result.append([with_num, without_num])
            dfs(nums)

        dfs(nums)
        return max(result[-1])
