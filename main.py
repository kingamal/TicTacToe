def row_winner(board):
    for row in board:
        all_equal = True
        piece = row[0]
        for entry in row:
            if entry == ' ' or piece != entry:
                all_equal = False
                break
        if all_equal:
            return True
    return False


def column_winner(board):
    for col in range(len(board[0])):
        all_equal = True
        piece = board[0][col]
        for row in board:
            if row[col] == ' ' or row[col] != piece:
                all_equal = False
                break
        if all_equal:
            return True
    return False


def diagonal_winner(board):
    all_equal1 = True
    all_equal2 = True
    topleft = board[0][0]
    topright = board[0][-1]
    for i in range(len(board)):
        if board[i][i] == ' ' or board[i][i] != topleft:
            all_equal1 = False
        if board[i][-i - 1] == ' ' or board[i][-i - 1] != topright:
            all_equal2 = False
    return all_equal1 or all_equal2