from typing import List

"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two 
different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one 
direction because they are too narrow.
Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of 
edges changed.
It's guaranteed that each city can reach city 0 after reorder.
"""


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(connection[0], connection[1]) for connection in connections}
        neighbours = {city: [] for city in range(n)}
        closer = set()
        reorders = 0

        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)
        print(neighbours)

        def visit(prev, city):
            nonlocal reorders
            if (prev, city) in edges:
                reorders += 1
            closer.add(city)
            for neighbour in neighbours[city]:
                if neighbour not in closer:
                    visit(city, neighbour)

        visit(0, 0)
        return reorders


if __name__ == '__main__':
    s = Solution()
    print(s.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
    # print(s.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
    # print(s.minReorder(5, [[1, 0], [1, 2], [2, 3], [4, 2]]))
    # print(s.minReorder(3, [[1, 0], [2, 0]]))
