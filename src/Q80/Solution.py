from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 0
        actual = 0

        for i, num in enumerate(nums):
            if num == curr:
                count += 1
            else:
                curr = num
                count = 1
            nums[i] = num

            if count <= 2:
                actual += 1
        return actual


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
