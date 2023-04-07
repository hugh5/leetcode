from typing import List

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can 
rob tonight without alerting the police.
"""


class Solution:
    """
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.
    """

    # Attempt 3: Refactored
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        return nums[len(nums) - 1]

    # Attempt 2: Using Dynamic Programming
    def rob2(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for n in nums:
            temp = max(n + prev1, prev2)
            prev1 = prev2
            prev2 = max(temp, prev2)
        return prev2

    # Attempt 1: Time Limit Exceeded
    def rob1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 7, 9, 3, 1]))
    print(s.rob([2, 1, 1, 2, 1, 1, 5]))
