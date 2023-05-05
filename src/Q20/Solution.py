"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {")": "(", "}": "{", "]": "["}
        i = 0
        for char in s:
            if char in m:
                if not stack or m[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[[{}]]{}"))
