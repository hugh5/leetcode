from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        start = None
        for j in range(height):
            if start:
                break
            for i in range(width):
                if grid[j][i] == 1:
                    start = (i, j)
                    break

        first = set()

        def dfs(i, j):
            if i < 0 or i >= width or j < 0 or j >= height:
                return
            if grid[j][i] == 0 or (i, j) in first:
                return
            first.add((i, j))
            for dy, dx in directions:
                dfs(i + dx, j + dy)

        dfs(start[0], start[1])
        visited = set()
        queue = list(first)

        def bfs():
            depth = 0
            while queue:
                for curr in range(len(queue)):
                    (i, j) = queue.pop(0)
                    if (i, j) in visited:
                        continue
                    if depth > 0 and grid[j][i] == 1:
                        return depth
                    else:
                        visited.add((i, j))
                    for dy, dx in directions:
                        if i + dx < 0 or i + dx >= width or j + dy < 0 or j + dy >= height:
                            continue
                        else:
                            queue.append((i + dx, j + dy))
                depth += 1

        return bfs() - 1


if __name__ == '__main__':
    s = Solution()
    print(s.shortestBridge([[0, 1],
                            [1, 0]]))
    print(s.shortestBridge([[0, 1, 0],
                            [0, 0, 0],
                            [0, 0, 1]]))
    print(s.shortestBridge([[1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 1, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1]]))
