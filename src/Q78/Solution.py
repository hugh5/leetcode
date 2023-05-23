from typing import List


class Solution:
    def helper(self, curr, options):
        result = []
        for i, option in enumerate(options):
            next = curr.copy()
            next.append(option)
            result.append(next)
            result.extend(self.helper(next, options[i+1:]))
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = self.helper([], nums)
        result.append([])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))
    print(s.subsets([1,2,3,4]))