import random
from typing import List

"""
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be 
equally likely as a result of the shuffling.
Implement the Solution class:
"""


class Solution:
    original = []
    nums = []

    """
    Solution(int[] nums) Initializes the object with the integer array nums.
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    """
    int[] reset() Resets the array to its original configuration and returns it.
    """

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    """
    int[] shuffle() Returns a random shuffling of the array.
    """

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums


if __name__ == '__main__':
    s = Solution([1, 2, 3])
    print(s.shuffle())
    print(s.reset())
    print(s.shuffle())
