from typing import List

"""
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing 
spots i and j have a distance j - i between them.
The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the 
sightseeing spots, minus the distance between them.
Return the maximum score of a pair of sightseeing spots.
"""


class Solution:
    """
    Input: values = [8,1,5,2,6]
    Output: 11
    Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

    Input: values = [1,2]
    Output: 2
    """

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxScore = 0
        spot1 = values[0]
        for i in range(1, len(values)):
            maxScore = max(maxScore, spot1 + values[i] - i)
            spot1 = max(spot1, values[i] + i)
        return maxScore


if __name__ == '__main__':
    s = Solution()
    print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
    print(s.maxScoreSightseeingPair([1, 2]))
