import heapq
from typing import List

"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
