from tictactoe import initial_state
import copy
import math

# Global Variables
X = "X"
O = "O"
EMPTY = None

initial_user = None
test_user = None


# Test function
def main ():

    # Testing boards
    initial_board = initial_state()

    test_board = [[X, X, EMPTY],
                  [EMPTY, O, O],
                  [EMPTY, EMPTY, O]]

    # Testing users
    initial_user = player(initial_board)
    test_user = player(test_board)
    moves = actions(test_board)

    print(moves)
    # print(initial_user)
    print(test_user)

    # Testing action
    movement = (1, 0)

    # new_board = result(test_board, movement)
    # print(new_board)

    # player_winner = winner(test_board)
    # print(player_winner)
    # state = terminal(test_board)
    # print(state)

    optimal = minimax(test_board)
    print(optimal)

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
                # checks board state to confirm game not tied
                if turns == 9:
                    return True
                
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

    # The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. 
    # If multiple moves are equally optimal, any of those moves is acceptable.

    # Player check / Highest value for "X"
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            a = min_value(result(board, action))
            if a > v:
                v = a
                options = action

    # Player check / Lowest value for "O"
    else: 
        v = math.inf
        for action in actions(board):
            a = max_value(result(board, action))
            if a < v:
                v = a
                options = action

    return options

def max_value(board):
    """
    Returns the optimal action for the max player "X".
    """
    # If terminal board is "TRUE"
    if terminal(board):
        return utility(board)

    # state max-value
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    """
    Returns the optimal action for the min player "O".
    """
    # If terminal board is "TRUE"
    if terminal(board):
        return utility(board)

    # state min-value
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


# Run program
main()