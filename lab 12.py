def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def simulate_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Preset sequence of moves: (row, col, player)
    moves = [(1, 1, 'X'), (0, 0, 'O'), (0, 1, 'X'), (2, 2, 'O')]
    
    for row, col, player in moves:
        board[row][col] = player
        print(f"Player {player} plays at ({row}, {col}):")
        print_board(board)
        print()

# Execution and Output
simulate_game()
