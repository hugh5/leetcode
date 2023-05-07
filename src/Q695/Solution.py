from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        height = len(grid)
        width = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(x, y) -> int:
            area = 1
            grid[y][x] = 0
            for dx, dy in directions:
                if 0 <= x + dx < width and 0 <= y + dy < height:
                    if grid[y+dy][x+dx] == 1:
                        area += bfs(x+dx, y+dy)
            return area

        for j in range(height):
            for i in range(width):
                if grid[j][i] == 1:
                    max_area = max(max_area, bfs(i, j))

        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
