"""Arquivo principal do programa"""

Board = list[list[int]]


def solve_sudoku(board: Board) -> Board:
    """
    Resolve um tabuleiro de sudoku.
    O tabuleiro deve ser uma lista de listas de inteiros.
    Cada lista interna representa uma linha do tabuleiro.
    Os elementos devem ser inteiros entre 0 e 9.
    Os zeros representam espaços vazios.

    """
    return board


def is_valid(board: Board) -> bool:
    """
    Checa se o tabuleiro é válido
    Um tabuleiro válido é um tabuleiro com 9 linhas, 9 colunas e 9 quadrantes.
    Todos os elementos devem ser inteiros entre 0 e 9.
    Cada linha, coluna e quadrante deve conter apenas um elemento de cada valor.
    O tabuleiro pode conter zeros, que representam espaços vazios.
    """
    if len(board) != 9:
        return False
    return True
