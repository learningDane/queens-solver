"""
8-Queens Problem Solver

This module implements functions to solve the classic 8-queens problem.
"""

def is_safe(board, row, col):
    """
    Check if a queen can be placed at position (row, col) without being threatened.

    A queen threatens another queen if they share the same row, column, or diagonal.

    Parameters:
        board (list): A 1D array where board[i] represents the column position
                     of the queen in row i
        row (int): The row to check
        col (int): The column to check

    Returns:
        bool: True if it's safe to place a queen at position (row, col), False otherwise
    """
    # TODO: Implement this function
    pass

def solve_queens(n=8):
    """
    Solve the n-queens problem and return a solution if one exists.

    Parameters:
        n (int): The size of the board and number of queens to place

    Returns:
        list or None: A 1D array representing a solution, where solution[i] is the
                     column position of the queen in row i, or None if no solution exists
    """
    # TODO: Implement this function using backtracking
    pass

def find_all_solutions(n=8):
    """
    Find all solutions to the n-queens problem.

    Parameters:
        n (int): The size of the board and number of queens to place

    Returns:
        list: A list of solutions, where each solution is a 1D array where
              solution[i] is the column position of the queen in row i
    """
    # TODO: Implement this function
    pass

def board_to_string(board:list[int])->str:
    """
    Convert a board configuration to a string representation.

    Parameters:
        board (list): A 1D array where board[i] represents the column position
                     of the queen in row i

    Returns:
        str: A string representation of the board with 'Q' for queens and '.' for empty squares
    """
    str = ""
    n = len(board)
    for i in board: # per ogni riga
        for j in range(0,n): # per ogni colonna
            if j == i:
                str += "Q"
            else:
                str += "."
        str += '\n' # newline
    return str

def count_solutions(n=8):
    """
    Count the number of solutions to the n-queens problem.

    Parameters:
        n (int): The size of the board and number of queens to place

    Returns:
        int: The number of solutions
    """
    # TODO: Implement this function
    # Hint: You can reuse find_all_solutions or implement a more efficient version
    pass

def is_valid_solution(board:list[int])->bool:
    """
    Check if a board configuration is a valid solution to the n-queens problem.

    Parameters:
        board (list): A 1D array where board[i] represents the column position
                     of the queen in row i

    Returns:
        bool: True if the board is a valid solution, False otherwise
    """
    # la condizione che ci sia una queen per riga è già soddisfatta
    # 1. controllo che la board sia > 3x3
    size = len(board)
    if size < 4:
        return False
    # 2. controlla che la board sia valida
    for i in board:
        if i >= size: # ogni numero deve essere minore della dimensione della board [0:size-1]
            return False
    # 3. controlla che ci sia UNA SOLA queen per colonna
    if len(set(board)) != size: # controllo che ogni numero appaia al più una volta
        return False
    # 4. controllo le diagonali
    # O(n)
    dif_set = set()
    sum_set = set()
    for i, val in enumerate(board): # per ogni riga
        dif = val - i # questo numero può apparire una volta sola nel set delle dif
        sum = val + i # questo numero può apparire una volta sola nel set delle sum
        if dif in dif_set or sum in sum_set: # il numero è gia presente in lista
            return False
        dif_set.add(dif)
        sum_set.add(sum)
    return True

print(is_valid_solution([5,0,4,1,7,2,6,3]))
