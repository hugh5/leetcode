from collections import Counter
from typing import List

"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following 
operation any number of times:
    Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to 
    nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.
"""


class Solution:
    """
    Input: nums = [3,4,2]
    Output: 6
    Explanation: You can perform the following operations:
    - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
    - Delete 2 to earn 2 points. nums = [].
    You earn a total of 6 points.

    Input: nums = [2,2,3,3,3,4]
    Output: 9
    Explanation: You can perform the following operations:
    - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
    - Delete a 3 again to earn 3 points. nums = [3].
    - Delete a 3 once more to earn 3 points. nums = [].
    You earn a total of 9 points.
    """

    # Attempt 2: Refactored to use two previous values instead
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1, earn2 = 0, nums[0] * count[nums[0]]
        for i in range(1, len(nums)):
            curr = nums[i] * count[nums[i]]
            if nums[i] - nums[i - 1] == 1:
                temp = max(earn1 + curr, earn2)
                earn1 = earn2
                earn2 = temp
            else:
                temp = max(earn1, earn2) + curr
                earn1 = earn2
                earn2 = temp
        return earn2

    # Attempt 1: DP using an Array to store previously calculated values
    def deleteAndEarn1(self, nums: List[int]) -> int:
        count = {}
        numbers = []
        for num in nums:
            mapping = count.pop(num, None)
            if mapping is None:
                count[num] = 1
                numbers.append(num)
            else:
                count[num] = mapping + 1
        numbers.sort()
        cache = numbers.copy()
        cache[0] = cache[0] * count[cache[0]]
        for i in range(1, len(numbers)):
            if numbers[i] - numbers[i - 1] == 1:
                cache[i] = max((cache[i - 2] if i > 1 else 0) + numbers[i] * count[numbers[i]], cache[i - 1])
            else:
                cache[i] = max(cache[i - 2] if i > 1 else 0, cache[i - 1]) + numbers[i] * count[numbers[i]]
        return cache[len(cache) - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.deleteAndEarn([3, 6, 6, 3, 5, 2]))
    print(s.deleteAndEarn([2, 3, 4]))
