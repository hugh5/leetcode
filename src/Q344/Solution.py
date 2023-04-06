from typing import List

"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    """
    Do not return anything, modify s in-place instead.
    """

    def reverseString(self, s: List[str]) -> None:
        for i in range(round(len(s) / 2)):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]


if __name__ == '__main__':
    s = Solution()
    l = ["h", "e", "l", "l", "o"]
    s.reverseString(l)
    print(l)
