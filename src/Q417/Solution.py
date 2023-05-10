from typing import List

"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches 
the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where 
heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and 
west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell 
adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell 
(ri, ci) to both the Pacific and Atlantic oceans.
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        height = len(heights)
        width = len(heights[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def bfs(x: int, y: int, seen: set):
            seen.add((x, y))
            for dy, dx in directions:
                if 0 <= x + dx < width and 0 <= y + dy < height and (x + dx, y + dy) not in seen:
                    if heights[y][x] <= heights[y + dy][x + dx]:
                        bfs(x + dx, y + dy, seen)

        for j in range(height):
            if j == 0:
                for i in range(width):
                    bfs(i, j, pacific)
            else:
                bfs(0, j, pacific)

        for i in range(width):
            if i == width - 1:
                for j in range(height):
                    bfs(i, j, atlantic)
            else:
                bfs(i, height-1, atlantic)

        return list(map(lambda t: [t[1],t[0]],pacific.intersection(atlantic)))


if __name__ == '__main__':
    s = Solution()
    print(s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
