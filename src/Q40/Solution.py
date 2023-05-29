from typing import List

"""
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],
        [1,2,5],
        [1,7],
        [2,6]]
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def combinations(curr, c_sum, options):
            if c_sum == target:
                result.append(curr.copy())
                return
            elif c_sum > target or not options:
                return

            prev = -1
            for i, num in enumerate(options):
                if num == prev:
                    continue
                else:
                    prev = num
                curr.append(num)
                combinations(curr, c_sum + num, options[i+1:])
                curr.pop()

        combinations([], 0, candidates)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
