from typing import List

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume 
all four edges of the grid are all surrounded by water.
"""


class Solution:
    """
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        num_islands = 0

        height = len(grid)
        width = len(grid[0])

        def explore(x, y):
            if grid[y][x] == "1":
                grid[y][x] = "0"
                for dx, dy in directions:
                    if 0 <= x + dx < width and 0 <= y + dy < height:
                        explore(x + dx, y + dy)

        for j in range(height):
            for i in range(width):
                if grid[j][i] == "1":
                    explore(i, j)
                    num_islands += 1

        return num_islands


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))
    print(s.numIslands([
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]))
