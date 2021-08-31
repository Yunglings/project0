def max_value(board):
    """
    Returns the optimal action for the max player (X).
    """
    
    # Possible legal moves
    states = list(actions(board))
    # Remaining turns
    num_states = len(states)
    i = 0
    # Utility 
    result_state = []
    utility_state = []
    x_opt = []

    # Determine optimum move index
    while i < num_states:
        state = states[i]
        result_state = result(board, state)
        # Utility(s): a function that, given a terminal state s, returns the utility value of the state: -1, 0, or 1.
        utility_state.append(utility(result_state))
        
        # Max-value state - "X" targets +1 
        x_max = max(utility_state)
        x_max_index = [v for v, x in enumerate(utility_state) if x == x_max]

        i += 1

    # Match optimum action
    for j in x_max_index:
        x_opt.append(states[j])
        return x_opt


def min_value(board):
    """
    Returns the optimal action for the min player (O).
    """
    
    # Possible legal moves
    states = list(actions(board))
    # Remaining turns
    num_states = len(states)
    i = 0
    # Utility 
    result_state = []
    utility_state = []
    O_opt = []

    # Determine optimum move index
    while i < num_states:
        state = states[i]
        result_state = result(board, state)
        # Utility(s): a function that, given a terminal state s, returns the utility value of the state: -1, 0, or 1.
        utility_state.append(utility(result_state))

        # Min-valve state - "O" targets -1 
        O_min = min(utility_state)
        O_min_index = [v for v, x in enumerate(utility_state) if x == O_min] 

        i += 1

    # Match optimum action
    for j in O_min_index:
        O_opt.append(states[j])
        return O_opt
