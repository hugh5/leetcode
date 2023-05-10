from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        for i in range(1,len(nums)+1):
            if i not in seen:
                return i
        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([3,4,-1,1]))
    print(s.firstMissingPositive([1,2,0]))