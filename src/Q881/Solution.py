from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while people[right] >= limit:
            boats += 1
            right -= 1
        while left <= right:
            boats += 1
            if left != right and people[right] + people[left] <= limit:
                left += 1
            right -= 1
        return boats


if __name__ == '__main__':
    s = Solution()
    # print(s.numRescueBoats([1, 7, 2, 6, 5, 7, 4, 2], 7))
    print(s.numRescueBoats([2, 49, 10, 7, 11, 41, 47, 2, 22, 6, 13, 12, 33, 18, 10, 26, 2, 6, 50, 10], 50))
