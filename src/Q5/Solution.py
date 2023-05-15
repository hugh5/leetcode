class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Sliding Window
        longest = 1
        length = len(s)
        left_i = 0
        right_i = 1

        for i in range(len(s) - 1):
            for j in range(2):
                left = i
                right = i + j
                while left >= 0 and right < length and s[left] == s[right]:
                    if right + 1 - left > longest:
                        longest = right - left + 1
                        left_i = left
                        right_i = right + 1
                    left -= 1
                    right += 1
        return s[left_i:right_i]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
