from typing import List

"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the 
array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""


class Solution:
    """
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
    """
    def canJump(self, nums: List[int]) -> bool:
        minCanJump = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= minCanJump:
                minCanJump = i
        return minCanJump == 0


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
    print(s.canJump([3, 2, 1, 0, 4]))
    print(s.canJump([1]))

