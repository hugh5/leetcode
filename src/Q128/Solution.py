from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        start_set = set()
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                start_set.add(num)
        for start in start_set:
            i = start + 1
            curr = 1
            while i in nums:
                i += 1
                curr += 1
                longest = max(longest, curr)

        return longest


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
