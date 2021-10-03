to_solve = [
    [0,0,5,3,0,0,0,0,0],
    [8,0,0,0,0,0,0,2,0],
    [0,7,0,0,1,0,5,0,0],
    [4,0,0,0,0,5,3,0,0],
    [0,1,0,0,7,0,0,0,6],
    [0,0,3,2,0,0,0,8,0],
    [0,6,0,5,0,0,0,0,9],
    [0,0,4,0,0,0,0,3,0],
    [0,0,0,0,0,9,7,0,0]
]

def display_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|" + " ", end="")
            if j != 8:
                print(str(board[i][j]) + " ", end="")
            else:
                print(str(board[i][j]))

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i,j)  # (row, column)
    return None

def is_valid_num(board, num, pos):
    row, column = pos
    # check row
    for i in range(len(board[row])):
        if board[row][i] == num and i != column:
            return False
    # check column
    for i in range(len(board)):
        if board[i][column] == num and i != row:
            return False
    # check box
    box_x = column - (column % 3)  # round to divisions of 3
    box_y = row - (row % 3)
    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve_board(board):
    find = find_empty(board)
    if not find:
        return True  # board solved
    else:
        row, column = find

    for i in range(1, 10):  # check all numbers from 1 to 9
        if is_valid_num(board, i, (row, column)):
            board[row][column] = i

            if solve_board(board):  # recursion
                return True  # board solved

            board[row][column] = 0

    return False

def main():
    print("Board before solving:")
    display_board(to_solve)
    print("***************************")
    solve_board(to_solve)
    print("Board after solving:")
    display_board(to_solve)

main()