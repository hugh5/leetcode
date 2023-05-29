from typing import List

"""
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permutations(curr, options: List[int]):
            if not options:
                result.append(curr.copy())
            else:
                for i in range(len(options)):
                    curr.append(options[i])
                    x = options.pop(i)
                    permutations(curr, options)
                    options.insert(i, x)
                    curr.pop()

        permutations([], nums)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
