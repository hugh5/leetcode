from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        e = len(nums) * (len(nums) + 1) // 2
        return e - s
