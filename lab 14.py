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

def alphabeta(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return -10 + depth
    if winner == 'O': return 10 - depth
    if all(cell != " " for row in board for cell in row): return 0
    
    if is_maximizing:
        max_eval = -float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = 'O'
                    eval = alphabeta(board, depth + 1, alpha, beta, False)
                    board[r][c] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = 'X'
                    eval = alphabeta(board, depth + 1, alpha, beta, True)
                    board[r][c] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

sample_board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'O']
]

# Execution and Output
ab_score = alphabeta(sample_board, 0, -float('inf'), float('inf'), True)
print("Alpha-Beta Pruned Evaluation Score:", ab_score)
