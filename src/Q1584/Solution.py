import heapq
import math
from collections import defaultdict
from typing import List, DefaultDict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        outgoing = defaultdict(list)
        pq = []
        for i, [x1, y1] in enumerate(points):
            for j, [x2, y2] in enumerate(points[i + 1:]):
                outgoing[i].append((j + i + 1, abs(x2 - x1) + abs(y2 - y1)))
                outgoing[j + i + 1].append((i, abs(x2 - x1) + abs(y2 - y1)))
            if i == 0:
                for n, d in outgoing[0]:
                    heapq.heappush(pq, (d, 0, n))

        cost = 0
        visited = {0}
        # print(outgoing)
        # print(pq)
        while len(visited) != len(points):
            d, i, j = heapq.heappop(pq)
            if i not in visited:
                visited.add(i)
                for n, dist in outgoing[i]:
                    heapq.heappush(pq, (dist, i, n))
            elif j not in visited:
                visited.add(j)
                for n, dist in outgoing[j]:
                    heapq.heappush(pq, (dist, j, n))
            else:
                continue
            cost += d
            print(d)


        return cost


if __name__ == '__main__':
    s = Solution()
    print(s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
    print(s.minCostConnectPoints([[0, 0]]))
    print(s.minCostConnectPoints([[2, -3], [-17, -8], [13, 8], [-17, -15]]))
