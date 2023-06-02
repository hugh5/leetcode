import math
from collections import defaultdict
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        outgoing = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = math.sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
                if d <= r1:
                    outgoing[i].append(j)
                if d <= r2:
                    outgoing[j].append(i)

        def dfs(node, visited):
            if node in visited:
                return 0
            else:
                visited.add(node)
                for n in outgoing[node]:
                    dfs(n, visited)
                return len(visited)

        max_depth = 0
        for i in range(len(bombs)):
            max_depth = max(max_depth, dfs(i, set()))
        return max_depth


if __name__ == '__main__':
    s = Solution()
    print(s.maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
    print(s.maximumDetonation([[4, 4, 3], [4, 4, 3]]))
