from typing import List

"""
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average 
greater than or equal to threshold.
"""
class Solution:
    """
    Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
    Output: 3

    Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
    Output: 6
    """
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        threshold *= k
        curr = sum(arr[:k-1]) + arr[-1]
        for right in range(k-1, len(arr)):
            curr -= arr[right-k]
            curr += arr[right]
            if curr >= threshold:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))
    print(s.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))