from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        j = 0
        while True:
            if len(strs[0]) == j:
                return prefix
            curr = strs[0][j]
            for str in strs[1:]:
                if len(str) == j or str[j] != curr:
                    return prefix
            prefix += strs[0][j]
            j += 1


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flower"]))