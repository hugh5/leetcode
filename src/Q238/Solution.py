from typing import List

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of 
nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    """
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums) - 1):
            result[i + 1] = nums[i] * result[i]
        post = 1
        for i in range(len(nums) - 1, 0, -1):
            post *= nums[i]
            result[i - 1] *= post
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
