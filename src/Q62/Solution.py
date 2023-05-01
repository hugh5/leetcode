"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot
tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at
any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
"""


class Solution:
    """
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down
    """

    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]

        for j in range(1, m):
            for i in range(1, n):
                grid[j][i] = grid[j-1][i] + grid[j][i-1]

        return grid[m-1][n-1]


if __name__ == '__main__':
    s = Solution()
    s.uniquePaths(3, 7)
