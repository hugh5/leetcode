from typing import List

"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        minimum = nums[high]

        while low <= high:
            i = (high + low) // 2
            if nums[i] > minimum:
                low = i + 1
            else:
                high = i - 1
                minimum = nums[i]

        return minimum


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([8, 16, 18, 22, 25, 1, 2, 3, 4, 7]))
    print(s.findMin([11, 13, 15, 17]))
