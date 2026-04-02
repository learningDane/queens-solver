"""
8-Queens Problem Solver (Object-Oriented Version)

This module implements functions and a class to solve the classic 8-queens problem.
"""

class Queens:
    """
    Classe per la risoluzione del problema delle 8 regine
    """
    def __init__(self, n: int = 8):
        self.n = n
        self.solutions = []
        self.board = [-1] * n

        # array booleani
        self.cols_used = [False] * n
        self.diags_used = [False] * (2 * n - 1)
        self.antidiags_used = [False] * (2 * n - 1)

        self.col_range0 = range((n + 1) // 2 - 1, -1, -1)
        self.n_meno = n - 1

        # sacrifico complessità spaziale per minore complessità temporale
        base = list(range(n))
        self.liste = [base]
        for i in range(1, n):
            lista = base.copy()
            lista[0], lista[i] = lista[i], lista[0]
            self.liste.append(lista)

        # differenzia solve_queens e find_all
        self._find_all_flag = False

    @staticmethod
    def is_safe(board: list[int], row: int, col: int) -> bool:
        for i in range(row):
            # controllo una colonna alla volta
            placed_col = board[i]
            # controlla le colonne
            if placed_col == col:
                return False
            # controlla diagonali
            if abs(placed_col - col) == abs(i - row):
                return False
        return True

    def solve(self) -> list[int] | None:
        """
        Wrapper per _find_solutions()
        """
        self._find_all_flag = False
        ret = self._find_solutions()
        if not ret:
            return None
        return ret[0]

    def find_all(self) -> list[list[int]]:
        """
        Wrapper per _find_solutions()
        """
        self._find_all_flag = True
        return self._find_solutions()

    def _find_solutions(self) -> list[list[int]]:
        match self.n:
            case 0 | 2 | 3: # no sol
                return []
            case 1:
                return [[0]] # [[]] perché solve poi indicizza

        find_all = self._find_all_flag
        self.solutions = []

        self._backtrack(0)

        if find_all: # devo specchiare le soluzioni
            mirrored = []
            for sol in self.solutions:
                mirror = [self.n - 1 - col for col in sol]
                if mirror not in self.solutions:
                    mirrored.append(mirror)
            self.solutions.extend(mirrored)

        return self.solutions

    def _backtrack(self, row: int) -> bool:
        if row == self.n:
            if self._find_all_flag:
                self.solutions.append(self.board.copy())
                return False
            else:
                self.solutions.append(self.board.copy())
                return True

        match row:
            case 0: # prima riga
                for col in self.col_range0:
                    self.board[row] = col
                    self.cols_used[col] = True
                    self.diags_used[col - row + self.n_meno] = True
                    self.antidiags_used[col + row] = True

                    if self._backtrack(row + 1):
                        return True # indifferente

                    # backtrack
                    self.cols_used[col] = False
                    self.diags_used[col - row + self.n_meno] = False
                    self.antidiags_used[col + row] = False
            case _: #altre righe
                # comincio con il provare la colonna tale che la nuova queen faccia una mossa ad L dalla scorsa
                L = (self.board[row - 1] + 2) % self.n
                for col in self.liste[L]:
                    if self.cols_used[col] or self.diags_used[col - row + self.n_meno] or self.antidiags_used[col + row]:
                        continue # questa colonna non va bene
                    else:
                        # posiziono queen
                        self.board[row] = col
                        self.cols_used[col] = True
                        self.diags_used[col - row + self.n_meno] = True
                        self.antidiags_used[col + row] = True

                        if self._backtrack(row + 1):
                            return True

                        self.cols_used[col] = False
                        self.diags_used[col - row + self.n_meno] = False
                        self.antidiags_used[col + row] = False
        return False

    @staticmethod
    def board_to_string(board: list[int]) -> str:
        stringa = ""
        n = len(board)
        for i in board: # per ogni riga
            for j in range(0, n): # per ogni colonna
                if j == i:
                    stringa += "Q"
                else:
                    stringa += "."
            stringa += '\n' # newline
        return stringa

    @staticmethod
    def is_valid_solution(board: list[int]) -> bool:
        size = len(board)
        match size:
            case 0 | 2 | 3:
                return False
            case 1:
                return not board[0]

        for i in board:
            if i >= size or i < 0:
                return False

        if len(set(board)) != size:
            return False

        dif_set = set()
        sum_set = set()
        for i, val in enumerate(board):
            dif = val - i
            sum = val + i
            if dif in dif_set or sum in sum_set:
                return False
            dif_set.add(dif)
            sum_set.add(sum)
        return True


# esposizione delle funzioni

def is_safe(board: list[int], row: int, col: int) -> bool:
    """Check if a queen can be placed at position (row, col) without being threatened."""
    return Queens.is_safe(board, row, col)

def solve_queens(n: int = 8) -> list[int] | None:
    """Solve the n-queens problem and return a solution if one exists."""
    return Queens(n).solve()

def find_all_solutions(n: int = 8) -> list[list[int]]:
    """Find all solutions to the n-queens problem."""
    return Queens(n).find_all()

def board_to_string(board: list[int]) -> str:
    """Convert a board configuration to a string representation."""
    return Queens.board_to_string(board)

def count_solutions(n: int = 8) -> int:
    """Count the number of solutions to the n-queens problem."""
    return len(find_all_solutions(n))

def is_valid_solution(board: list[int]) -> bool:
    """Check if a board configuration is a valid solution to the n-queens problem."""
    return Queens.is_valid_solution(board)
