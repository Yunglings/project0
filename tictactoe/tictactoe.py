"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    # Initialise turns
    turns = 0

    # Initialise_state - Turns check
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                turns += 1
                # initial_state returns "X" for first move
                if turns == 9:
                    return X


    # Turns check
    # Any return value is acceptable if a terminal board is provided as input.
    if turns % 2 == 0:
        return O
    else: 
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #Initialise set
    moves = set()

    # Returns tuple (i, j)

    # i corresponds to the row of the move (0, 1, or 2) 
    for i in range(3):
        # j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    
    # Move options returned
    return(moves)

    # Possible moves are any cells on the board that do not already have an X or an O in them.
    # Any return value is acceptable if a terminal board is provided as input.


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Set action position
    row = action[0]
    column = action[1]

    # If action is not a valid action for the board, your program should raise an exception.
    if board[row][column] != EMPTY:
        raise Exception("action not valid")

    # The original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation.
    else:
        deep_copy_board = copy.deepcopy(board)
        # deep copy of the board first before making any changes.
        # updating a cell in board itself is not a correct implementation of the result function.
        
        # The returned board state should be the board that would result from taking the original 
        # input board, and letting the player whose turn it is make their move at the cell indicated by the input action. 

        # Player to be determined
        move = player(deep_copy_board)
        for action in deep_copy_board: 
            # Removes cell chosen by player and inserts players move 
            deep_copy_board[row][column] = move
            return deep_copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).

    # If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.

    # One can win the game with three of their moves in a row horizontally, vertically, or diagonally.

    # Horizontal win
    if board[0][0] == X and board[0][1] == X and board [0][2] == X or board[1][0] == X and board[1][1] == X and board [1][2] == X or board[2][0] == X and board[2][1] == X and board [2][2] == X:
        return X
    elif board[0][0] == O and board[0][1] == O and board [0][2] == O or board[1][0] == O and board[1][1] == O and board [1][2] == O or board[2][0] == O and board[2][1] == O and board [2][2] == O:
        return O

    # Vertical win
    if board [0][0] == X and board [1][0] == X and board [2][0] == X or board [0][1] == X and board [1][1] == X and board [2][1] == X or board [0][2] == X and board [1][2] == X and board [2][2] == X:
        return X
    elif board [0][0] == O and board [1][0] == O and board [2][0] == O or board [0][1] == O and board [1][1] == O and board [2][1] == O or board [0][2] == O and board [1][2] == O and board [2][2] == O:
        return O

    # Diagonal win
    if board[0][0] == X and board[1][1] == X and board [2][2] == X or board[0][2] == X and board[1][1] == X and board [2][0] == X:
        return  X
    elif board[0][0] == O and board[1][1] == O and board [2][2] == O or board[0][2] == O and board[1][1] == O and board [2][0] == O:
        return  O

    # If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
    else: 
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Initialise turns
    turns = 0

    # Turns check
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                turns += 1
                # checks board to confirm game not tied
                if turns == 9:
                    return True

    # Winner check            
    if winner(board) != None:
        return True
    
    # return False if the game is still in progress.
    else: 
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # assumed utility will only be called on a board if terminal(board) is True
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else: 
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If the board is a terminal board, the minimax function should return None.
    if terminal(board) == True:
        return None

    # If multiple moves are equally optimal, any of those moves is acceptable.

    # Player check / Highest value for "X"
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))
            if k > v:
                v = k
                options = action

    # Player check / Lowest value for "O"
    else: 
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))
            if k < v:
                v = k
                options = action

    # The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. 
    return options

def max_value(board):
    """
    Returns the optimal action for the max player "X".
    """
    if terminal(board):
        return utility(board)
        
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    """
    Returns the optimal action for the min player "O".
    """
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
    