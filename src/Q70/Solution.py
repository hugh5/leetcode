"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        results = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            if i == 1:
                results[i] = 1
            elif i == 2:
                results[i] = 2
            else:
                results[i] = results[i - 1] + results[i - 2]
        return results[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))
