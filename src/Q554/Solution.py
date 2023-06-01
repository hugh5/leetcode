from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = defaultdict(int)
        gaps[0] = 0
        for row in wall:
            c = 0
            for brick in row[:-1]:
                c += brick
                gaps[c] += 1
        return len(wall) - max(gaps.values())


if __name__ == '__main__':
    s = Solution()
    print(s.leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]))
