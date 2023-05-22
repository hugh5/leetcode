from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr_sum = sum(cardPoints[:k])
        max_score = curr_sum
        for i in range(k-1, -1, -1):
            curr_sum -= cardPoints[i]
            curr_sum -= cardPoints[i-k]
            # curr_sum += cardPoints[k+i+1]
            max_score = max(max_score, curr_sum)
        return max_score

if __name__ == '__main__':
    s = Solution()
    print(s.maxScore([1,2,3,4,5,6,1], 3))
    print(s.maxScore([2,2,2], 2))
    print(s.maxScore([9,7,7,9,7,7,9], 7))
