
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        width = len(word1)
        height = len(word2)

        result = [[width + height - i - j for i in range(width + 1)] for j in range(height + 1)]
        for j in range(height - 1, -1, -1):
            for i in range(width - 1, -1, -1):
                if word1[i] == word2[j]:
                    result[j][i] = result[j + 1][i + 1]
                else:
                    result[j][i] = 1 + min(result[j + 1][i], result[j + 1][i + 1], result[j][i + 1])
        for row in result:
            print(row)
        return result[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("horse", "ros"))
    print(s.minDistance("intention", "execution"))
