sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_valid(num, row, col):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
        if sudoku[i][col] == num:
            return False
        if sudoku[3*(row//3)+i//3][3*(col//3)+i%3] == num:
            return False
    return True

def solve():
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(num, row, col):
                        sudoku[row][col] = num
                        if solve():
                            return True
                        sudoku[row][col] = 0
                return False
    return True

if __name__ == "__main__":
    # Removed input reading; using hardcoded puzzle
    if solve():
        for row in sudoku:
            print(*row)
    else:
        print("No solution exists")