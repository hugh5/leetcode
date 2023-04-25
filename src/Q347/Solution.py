from collections import Counter
from typing import List

"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
"""


class Solution:
    """
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Input: nums = [1], k = 1
    Output: [1]
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        size = max(count.values()) + 1
        x = [[] for i in range(size)]
        for key, val in count.items():
            x[val].append(key)
        result = []
        i = size - 1
        while len(result) < k:
            if x[i]:
                result.append(x[i].pop())
            else:
                i -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
