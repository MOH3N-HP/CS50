"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None
NAW = "Not a winner"


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if (cell == X):
                x_count += 1
            elif (cell == O):
                o_count += 1

    if (x_count == o_count):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if (cell == EMPTY):
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    temp[i][j] = player(board)

    return temp


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def check_line(a, b, c):
        return a == b == c and a != EMPTY

    for i in range(3):
        if check_line(board[i][0], board[i][1], board[i][2]):
            return board[i][0]

    for j in range(3):
        if check_line(board[0][j], board[1][j], board[2][j]):
            return board[0][j]

    if check_line(board[0][0], board[1][1], board[2][2]):
        return board[0][0]

    if check_line(board[0][2], board[1][1], board[2][0]):
        return board[0][2]

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return None

    return NAW


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    act = None
    if player(board) == X:
        score = -100
        for action in actions(board):
            tmp_score = Max_value(result(board, action))
            if tmp_score > score:
                score = tmp_score
                act = action
    else:
        score = 100
        for action in actions(board):
            tmp_score = Min_Value(result(board, action))
            if tmp_score < score:
                score = tmp_score
                act = action

    return act


def Max_value(board):
    if terminal(board):
        return utility(board)

    v = -float('inf')
    for action in actions(board):
        v = max(v, Min_Value(result(board, action)))
        if v == 1:
            return v

    return v


def Min_Value(board):
    if terminal(board):
        return utility(board)

    v = float('inf')
    for action in actions(board):
        v = min(v, Max_value(result(board, action)))
        if v == -1:
            return v

    return v
