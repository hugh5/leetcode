
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {c: 0 for c in set(s)}
        longest = 1
        left = 0
        max_occur = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_occur = max(max_occur, count[s[right]])
            if right - left - max_occur + 1 > k:
                count[s[left]] -= 1
                left += 1
            print(f"Left={left}, Right={right}")
            longest = max(longest, right - left + 1)
        return longest




if __name__ == '__main__':
    s = Solution()
    print(s.characterReplacement("ABAB", 2))
    print(s.characterReplacement("AABABBA", 1))
    print(s.characterReplacement("AAAA", 0))
