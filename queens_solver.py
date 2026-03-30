"""
8-Queens Problem Solver

This module implements functions to solve the classic 8-queens problem.
"""
cols_set = set()
diags_set = set()
antidiags_set = set()

def is_safe(board: list[int], row:int, col:int) -> bool:
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
    diag = col - row
    antidiag = col + row
    if diag in diags_set or antidiag in antidiags_set or col in cols_set:
        return False
    else:
        return True

def solve_queens(n:int=8) -> list[int] | None:
    """
    Solve the n-queens problem and return a solution if one exists.

    Parameters:
        n (int): The size of the board and number of queens to place

    Returns:
        list or None: A 1D array representing a solution, where solution[i] is the
                     column position of the queen in row i, or None if no solution exists
    """
    match n:
        case 0 | 2 | 3:
            return []
        case 1:
            return [0]

    board = [-1] * n
    row = 0
    solutions = []
    _reset_sets()

    pass

def _trova_safe(n:int, board: list[int], row:int) -> bool:
    for i in range(board[row]+1,n):
        if is_safe(board, row, i): # trovata colonna safe per questa row
            board[row] = i
            cols_set.add(i)
            diags_set.add(i-row)
            antidiags_set.add(i+row)
            return True
    return False

def _reset_sets():
    global cols_set
    global diags_set
    global antidiags_set
    cols_set = set()
    diags_set = set()
    antidiags_set = set()

def find_all_solutions(n=8) -> None:#list:
    """
    Find all solutions to the n-queens problem.

    Parameters:
        n (int): The size of the board and number of queens to place

    Returns:
        list: A list of solutions, where each solution is a 1D array where
              solution[i] is the column position of the queen in row i
    """
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
    stringa = ""
    n = len(board)
    for i in board: # per ogni riga
        for j in range(0,n): # per ogni colonna
            if j == i:
                stringa += "Q"
            else:
                stringa += "."
        stringa += '\n' # newline
    return stringa

def count_solutions(n=8):
    """
    Count the number of solutions to the n-queens problem.

    Parameters:
        n (int): The size of the board and number of queens to place

    Returns:
        int: The number of solutions
    """
    return len(find_all_solutions(n))

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
    # -------
    match size:
        case 0:
            return False
        case 2:
            return False
        case 3:
            return False
        case 1:
            return not board[0]

    # 2. controlla che la board sia valida
    for i in board:
        if i >= size or i < 0: # ogni numero deve essere minore della dimensione della board [0:size-1]
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
