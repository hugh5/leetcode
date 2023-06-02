from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def back_track(curr, count, close):
            if count == n and close == 0:
                result.append(curr)
            else:
                if count < n:
                    back_track(curr + "(", count + 1, close + 1)

                if close > 0:
                    back_track(curr + ")", count, close - 1)

        back_track("", 0, 0)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
