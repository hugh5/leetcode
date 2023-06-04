from collections import defaultdict
from typing import List, DefaultDict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        outgoing: DefaultDict[int, List[int]] = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected[0])):
                if isConnected[i][j]:
                    outgoing[i].append(j)
                    outgoing[j].append(i)

        count = 0
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for e in outgoing[i]:
                dfs(e)

        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                dfs(i)
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]))
