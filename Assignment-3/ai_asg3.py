def utility(board):
    # Utility function to calculate the score for Player 1 (black coins)
    return board.count('B') + board.count('W')


def terminal_state(board):
    # Check if the board has no empty blocks
    return '0' not in board


def actions(board):
    # Return a list of indices where a player can place a coin
    return [i for i, block in enumerate(board) if block == '0']


def result(board, action, player):
    # Update the board after a player makes a move
    new_board = list(board)
    new_board[action] = 'B' if player == 1 else 'W'

    # Update the coins in continuity
    for i in range(len(new_board)):
        if new_board[i] == 'B' and (i > 0 and new_board[i - 1] == 'W'):
            new_board[i] = 'W'
        elif new_board[i] == 'W' and (i > 0 and new_board[i - 1] == 'B'):
            new_board[i] = 'B'

    return ''.join(new_board)


def min_value(board):
    if terminal_state(board):
        return utility(board)

    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action, 2)))
    return v


def max_value(board):
    if terminal_state(board):
        return utility(board)

    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action, 1)))
    return v


def minimax_decision(board):
    # Find the best move for Player 1 (MAX)
    best_value = float('-inf')
    best_action = None

    for action in actions(board):
        value = min_value(result(board, action, 1))
        if value > best_value:
            best_value = value
            best_action = action

    return best_action


def example_game():
    # Example board: "0000W00BBW0"
    board = "0000W00BBW0"
    utility_player_1 = utility(board)

    print(f"Initial Board: {board}")
    while not terminal_state(board):
        # Player 1 (MAX) makes a move
        best_move = minimax_decision(board)
        board = result(board, best_move, 1)
        print(f"Player 1's move: {best_move}, Updated Board: {board}")

    # Calculate the utility for Player 1
    print(f"Utility of Player 1: {utility_player_1}")

# Call the example_game function without ()
example_game()
