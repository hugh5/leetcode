class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longest = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        for j in range(len(text2) - 1, -1, -1):
            for i in range(len(text1) - 1, -1, -1):
                if text1[i] == text2[j]:
                    longest[j][i] = longest[j + 1][i + 1] + 1
                else:
                    longest[j][i] = max(longest[j + 1][i], longest[j][i + 1])
        return longest[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence("adbcde", "ace"))
    print(s.longestCommonSubsequence("yirvuaewoawe", "aviorewyubhe"))
