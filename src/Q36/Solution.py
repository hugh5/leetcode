from typing import List

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        positions = set()
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == ".":
                    continue

                if f"{board[y][x]} in row {y}" in positions:
                    return False
                positions.add(f"{board[y][x]} in row {y}")

                if f"{board[y][x]} in col {x}" in positions:
                    return False
                positions.add(f"{board[y][x]} in col {x}")

                grid = (y // 3) * 3 + x // 3
                if f"{board[y][x]} in grid {grid}" in positions:
                    return False
                positions.add(f"{board[y][x]} in grid {grid}")
        return True


if __name__ == '__main__':
    s = Solution()
    board = [["5", "3", ".",       ".", "7", ".",      ".", ".", "."],  # 0 - 2
             ["6", ".", ".",       "1", "9", "5",      ".", ".", "."],
             [".", "9", "8",       ".", ".", ".",      ".", "6", "."],

             ["8", ".", ".",       ".", "6", ".",      ".", ".", "3"],  # 3 - 5
             ["4", ".", ".",       "8", ".", "3",      ".", ".", "1"],
             ["7", ".", ".",       ".", "2", ".",      ".", ".", "6"],

             [".", "6", ".",       ".", ".", ".",      "2", "8", "."],  # 6 - 8
             [".", ".", ".",       "4", "1", "9",      ".", ".", "5"],
             [".", ".", ".",       ".", "8", ".",      ".", "7", "9"]]
    print(s.isValidSudoku(board))
