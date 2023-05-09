from typing import List


"""
Companies
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.
"""

class Solution:
    """
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        curr = []
        def helper(a):
            if len(curr) == k:
                result.append(curr.copy())
            else:
                for j in range(a, n+1):
                    curr.append(j)
                    helper(j+1)
                    curr.pop()

        helper(1)
        return result



if __name__ == '__main__':
    s = Solution()
    print(s.combine(4,2))