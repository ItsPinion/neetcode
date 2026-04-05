class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        col: dict[int, set[str]] = {}
        row: dict[int, set[str]] = {}
        grid: dict[tuple[int, int], set[str]] = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                digit: str = board[i][j]
                if digit != ".":
                    if not row.get(i):
                        row[i] = set()
                    if not col.get(j):
                        col[j] = set()
                    if not grid.get((i // 3, j // 3)):
                        grid[(i // 3, j // 3)] = set()

                    if digit in row[i]:
                        return False
                    if digit in col[j]:
                        return False
                    if digit in grid[(i // 3, j // 3)]:
                        return False

                    row[i].add(digit)
                    col[j].add(digit)
                    grid[(i // 3, j // 3)].add(digit)

        return True


solution = Solution()
board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(solution.isValidSudoku(board))
