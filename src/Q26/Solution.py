"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
element appears only once. The relative order of the elements should be kept the same. Then return the number of
unique elements in nums.

Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were
present in nums initially. The remaining elements of nums are not important as well as the size of nums.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            unique.add(num)
        for count, num in enumerate(sorted(unique)):
            nums.__setitem__(count, num)
        return len(unique)


if __name__ == '__main__':
    s = Solution()
    l = list((1, 1, 1, 2, 3, 4, 4, 5, 6, 7))
    print(s.removeDuplicates(l))
    print(l)
