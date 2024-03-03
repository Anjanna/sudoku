class Solution:
    def __init__(self):
        self._is_solved = False

    def solve_sudoku(self, board):
        def dfs(position):
            if position == len(empty_positions):
                self._is_solved = True
                return
            row, col = empty_positions[position]
            for value in range(9):
                if (not rows_used[row][value] and
                    not cols_used[col][value] and
                    not boxes_used[row//3][col//3][value]):
                    rows_used[row][value] = cols_used[col][value] = boxes_used[row//3][col//3][value] = True
                    board[row][col] = str(value + 1)
                    dfs(position+1)
                    rows_used[row][value] = cols_used[col][value] = boxes_used[row//3][col//3][value] = False
                if self._is_solved:
                    return
        rows_used = [[False] * 9 for _ in range(9)]
        cols_used = [[False] * 9 for _ in range(9)]
        boxes_used = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        empty_positions = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_positions.append((r, c))
                else:
                    value = int(board[r][c]) - 1
                    rows_used[r][value] = cols_used[c][value] = boxes_used[r//3][c//3][value] = True
        dfs(0)

    def print_sudoku_board(self, board):
        for r in range(9):
            if r%3==0:
                print("----------------------")
            for c in range(9):
                if c%3 == 0:
                    print("|", end="")
                print(board[r][c], end=" ")
            print("|", end="")
            print("")
        print("----------------------")

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution = Solution()
print("Initial Sudoku Board")
solution.print_sudoku_board(board)
solution.solve_sudoku(board)
print("Solved Sudoku Board")
solution.print_sudoku_board(board)
