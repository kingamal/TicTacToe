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