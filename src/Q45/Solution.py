from typing import List

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at 
nums[i], you can jump to any nums[i + j] where:
    0 <= j <= nums[i] and
    i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach 
nums[n - 1].
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currEnd = 0
        nextEnd = 0
        i = 0
        while currEnd < len(nums) - 1:
            nextEnd = max(nextEnd, i + nums[i])
            if i == currEnd:
                jumps += 1
                currEnd = nextEnd
            i += 1
        return jumps


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
    print(s.jump([2, 3, 0, 1, 4]))
    print(s.jump([1, 2, 2, 0, 4]))
