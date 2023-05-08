class Solution:

    """
    A message containing letters from A-Z can be encoded into numbers using the following mapping:
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the
    mapping above (there may be multiple ways). For example, "11106" can be mapped into:
        "AAJF" with the grouping (1 1 10 6)
        "KJF" with the grouping (11 10 6)
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

    Given a string s containing only digits, return the number of ways to decode it.
    The test cases are generated so that the answer fits in a 32-bit integer.
    """
    def numDecodings(self, s: str) -> int:
        prev1 = 0
        prev2 = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                prev2 = prev1
                prev1 = 0
            elif i == len(s) - 1:
                prev1 = 1
            else:
                if int(s[i] + s[i + 1]) <= 26:
                    if i + 1 == len(s) - 1:
                        prev1 = 1 + prev1
                        prev2 = prev1 - 1
                    else:
                        temp = prev1
                        prev1 = prev1 + prev2
                        prev2 = temp
                else:
                    prev2 = prev1
        return prev1

    def numDecodingsCache(self, s: str) -> int:
        cache = [0] * len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                cache[i] = 0
            elif i == len(s) - 1:
                cache[i] = 1
            else:
                if int(s[i] + s[i + 1]) <= 26:
                    if i + 1 == len(s) - 1:
                        cache[i] = 1 + cache[i + 1]
                    else:
                        cache[i] = cache[i + 1] + cache[i + 2]
                else:
                    cache[i] = cache[i + 1]
        return cache[0]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("2194123"))
