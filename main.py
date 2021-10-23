def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)

def winning_line(strings):
    piece = strings[0]
    if piece == ' ':
        return False
    for entry in strings:
        if piece != entry:
            return False
    return True

def row_winner(board):
    for row in board:
        if winning_line(row):
            return True
    return False

def column_winner(board):
    for col in range(len(board[0])):
        column = []
        for row in board:
            column.append(row[col])
        if winning_line(column):
            return True
    return False

def diagonal_winner(board):
    diagonal1 = []
    diagonal2 = []
    for i in range(len(board)):
        diagonal1.append(board[i][i])
        diagonal2.append(board[i][-i-1])
    return winning_line(diagonal1) or winning_line(diagonal2)


def format_board(board):
    first_row = ' '
    for i in range(len(board)):
        first_row += str(i + 1)
    joined_rows = [first_row]
    for i in range(len(board)):
        joined_row = str(i + 1) + ''.join(board[i])
        joined_rows.append(joined_row)
    return "\n".join(joined_rows)