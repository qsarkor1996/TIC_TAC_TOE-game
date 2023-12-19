def game_board(board):
    for row in board:
        print('|'.join(row))
        print("-" * 5)


def checking_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def get_move(player):
    while True:
        move = input(f"Player {player}, enter your move (row, col): ")
        row, col = map(int, move.split())
        if 0 <= row < 3 and 0 <= col < 3:
            return row, col
        else:
            print("Invalid move, Please try again.")


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        game_board(board)
        row, col = get_move(current_player)

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print('This sell is already taken. Please try again.')
            continue

        if checking_winner(board, current_player):
            game_board(board)
            print(f"Player {current_player} is winner!")
            break

        if is_board_full(board):
            game_board(board)
            print("It is tie")
            break

        current_player = 'O' if current_player == 'X' else 'X'


tic_tac_toe()
