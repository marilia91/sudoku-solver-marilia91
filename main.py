def solve_sudoku(boards: list[list[int]]) -> list[list[int]]:
    def resolve(boards: list[list[int]]) -> bool:
        i, j = Board(boards)
        if i == None or j == None:
            return True 

        for num in range(1, 10):
            boards[i][j] = num 

            if is_valid(boards) and resolve(boards): 
                return True

            boards[i][j] = 0 

        return False

    if resolve(boards):
        return boards
    raise ValueError

def is_valid(boards: list[list[int]]) -> bool:
    for i in range(9):
        for j in range(9):
            num = boards[i][j]
            if num != 0:
                for col in range(9):
                    if col != j and boards[i][col] == num:
                        return False

                for row in range(9):
                    if row != i and boards[row][j] == num:
                        return False
                start_row = 3 * (i // 3) 
                start_col = 3 * (j // 3)
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        if (row != i or col != j) and boards[row][col] == num:
                            return False

    return True

def Board(boards: list[list[int]]) -> tuple[int, int]:
    for i in range(9):
        for j in range(9):
            if boards[i][j] == 0:
                return i, j
    return None, None
