from typing import List

"""
You are given an m x n integer matrix matrix with the following two properties:
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        length = len(matrix[0])

        low = 0
        high = height-1
        mid = high // 2
        while True:
            if high >= low:
                break
            elif target < matrix[mid][0]:
                high = mid - 1
                mid = (high + low) // 2
            elif target > matrix[mid][length-1]:
                low = mid + 1
                mid = (high + low) // 2
            else:
                break

        row = mid
        low = 0
        high = length-1
        mid = high // 2
        while True:
            if low >= high:
                return matrix[row][mid] == target
            elif target < matrix[row][mid]:
                high = mid - 1
                mid = (high + low) // 2
            elif target > matrix[row][mid]:
                low = mid + 1
                mid = (high + low) // 2
            else:
                return True


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1],[3]], 0))
