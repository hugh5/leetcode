from typing import List

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        curr = set()
        for right in range(len(nums)):
            if right-k-1 >= 0:
                curr.remove(nums[right-k-1])
            if nums[right] in curr:
                return True
            curr.add(nums[right])
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1], 3))
    print(s.containsNearbyDuplicate([1,0,1,1], 1))
    print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))