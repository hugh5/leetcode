from typing import List

"""
Given an integer array nums, find the
subarray
with the largest sum, and return its sum.
"""


class Solution:
    """
    Input 1: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            maxSum = max(maxSum, nums[i])
        print(nums)
        return maxSum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([5, 4, -1, 7, 8]))
