from typing import List

"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that 
they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1 = 0
        i2 = len(numbers) - 1

        while i1 < i2:
            if numbers[i1] + numbers [i2] > target:
                i2 -= 1
            elif numbers[i1] + numbers[i2] < target:
                i1 += 1
            else:
                return [i1+1, i2+1]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))