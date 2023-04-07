from typing import List

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two 
adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can 
rob tonight without alerting the police.
"""


class Solution:
    """
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    Input: nums = [1,2,3]
    Output: 3
    """

    def rob1(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        return nums[len(nums) - 1]

    def rob(self, nums: List[int]) -> int:
        res1 = self.rob1(nums[:len(nums) - 1])
        res2 = self.rob1(nums[1:])
        return max(res1, res2)


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2, 3, 2]))
