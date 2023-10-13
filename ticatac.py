import math, copy


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def is_game_over(board):
    for row in board:
        if row.count("X") == 3 or row.count("O") == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1] != " "

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def evaluate_board(board):
    if is_game_over(board):
        return -1 if board[1][1] == "X" else 1
    elif is_board_full(board):
        return 0
    else:
        return None

def make_move(board, player, move):
    i, j = move
    board[i][j] = player

def undo_move(board, move):
    i, j = move
    board[i][j] = " "

def computer_move(board):
    best_value = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf

    for move in available_moves(board):
        make_move(board, "O", move)
        move_value = alphabeta(board, 9, alpha, beta, False)
        undo_move(board, move)

        if move_value > best_value:
            best_value = move_value
            best_move = move

        alpha = max(alpha, best_value)

    return best_move

def alphabeta(state, depth, alpha, beta, isMaxPlayer):
    if depth == 0 or is_game_over(state):
        return evaluate_board(state)

    if isMaxPlayer: 
        v_max = -math.inf
        for pos in available_moves(state):
            child = copy.deepcopy(state)
            make_move(child, "X", pos)
            v = alphabeta(child, depth - 1, alpha, beta, False)
            v_max = max(v_max, v)
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v_max
    else: 
        v_min = math.inf
        for pos in available_moves(state):
            child = copy.deepcopy(state)
            make_move(child, "O", pos)
            v = alphabeta(child, depth - 1, alpha, beta, True)
            v_min = min(v_min, v)
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v_min

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while not is_game_over(board) and not is_board_full(board):
        print_board(board)
        user_move = tuple(map(int, input("Enter your move (row and column separated by space): ").split()))
        if board[user_move[0]][user_move[1]] != " ":
            print("Invalid move. Cell is already occupied.")
            continue
        make_move(board, "X", user_move)

        if is_game_over(board):
            print("You won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        computer_move_result = computer_move(board)
        make_move(board, "O", computer_move_result)

        if is_game_over(board):
            print_board(board)
            print("You lost!")
            break

    if not is_game_over(board) and is_board_full(board):
        print("It's a draw!")

if __name__ == "__main__":
    play_tic_tac_toe()
