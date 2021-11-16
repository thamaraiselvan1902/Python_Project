def sudoku(puzzle):
    for r in range(9):
        for c in range(9):
            print(puzzle[r][c],end = "|")
        print()


def solve(puzzle, row, col, guess):
    for x in range(9):
        if puzzle[row][x] == guess:
            return False

    for x in range(9):
        if puzzle[x][col] == guess:
            return False

    rowstart = row - row % 3
    colstart = col - col % 3
    for r in range(3):
        for c in range(3):
            if puzzle[r + rowstart][c + colstart] == guess:
                return False

    return True

def number(puzzle, row, col):
    if(row == 9 - 1 and col == 9):
        return True
    if col == 9:
        row += 1
        col = 0
    if puzzle[row][col] > 0:
        return number(puzzle, row, col + 1)
    for guess in range(1, 9 + 1, 1):
        
        if solve(puzzle, row, col, guess):
            puzzle[row][col] = guess
            if number(puzzle, row, col + 1):
                return True
        puzzle[row][col] = 0
    return False


'''0 means the cells where no value is assigned'''

puzzle = [[0, 0, 4, 0, 0, 0, 0, 0, 0],
        [2, 0, 5, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 3],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 6, 0],
        [1, 0, 8, 0, 0, 5, 3, 0, 0],
        [0, 3, 0, 0, 0, 9, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 2, 0, 0],
        [9, 0, 2, 0, 5, 0, 0, 0, 7]]

if (number(puzzle, 0, 0)):
    sudoku(puzzle)
else:
    print(" ****Invalid****")
