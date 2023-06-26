"""Testa o arquivo main.py"""

import unittest  # para criar testes unitários

from main import Board, is_valid, solve_sudoku


class TestSudoku(unittest.TestCase):
    """Classe para testar o arquivo main.py"""

    def setUp(self):
        """Cria os tabuleiros para testar"""
        self.boards: list[dict[str, Board]] = []

        puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        solution = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]
        self.boards.append({"puzzle": puzzle, "solution": solution})

        puzzle = [
            [0, 4, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 0, 4, 0, 0, 6, 0, 3],
            [0, 0, 1, 0, 7, 9, 0, 2, 0],
            [7, 0, 0, 0, 0, 8, 0, 0, 2],
            [9, 0, 0, 0, 3, 0, 0, 0, 1],
            [6, 0, 0, 9, 0, 0, 0, 0, 7],
            [0, 7, 0, 3, 1, 0, 8, 0, 0],
            [1, 0, 9, 0, 0, 4, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 1, 0],
        ]

        solution = [
            [2, 4, 7, 6, 5, 3, 1, 9, 8],
            [8, 9, 5, 4, 2, 1, 6, 7, 3],
            [3, 6, 1, 8, 7, 9, 4, 2, 5],
            [7, 5, 3, 1, 6, 8, 9, 4, 2],
            [9, 8, 4, 2, 3, 7, 5, 6, 1],
            [6, 1, 2, 9, 4, 5, 3, 8, 7],
            [4, 7, 6, 3, 1, 2, 8, 5, 9],
            [1, 2, 9, 5, 8, 4, 7, 3, 6],
            [5, 3, 8, 7, 9, 6, 2, 1, 4],
        ]
        self.boards.append({"puzzle": puzzle, "solution": solution})

    def test_example_incomplete(self):
        """Testa o exemplo do README.md"""
        self.assertEqual(is_valid(self.boards[0]["puzzle"]), True)
        self.assertEqual(
            solve_sudoku(self.boards[0]["puzzle"]), self.boards[0]["solution"]
        )

    def test_hard_puzzle(self):
        """Testa um tabuleiro difícil"""
        # Hard Puzzle 5,037,319,511 from https://www.websudoku.com/?level=3
        self.assertEqual(is_valid(self.boards[1]["puzzle"]), True)
        self.assertEqual(
            solve_sudoku(self.boards[1]["puzzle"]), self.boards[1]["solution"]
        )

    def test_impossible_boards(self):
        """Testa alguns tabuleiros impossíveis"""
        board = [[1 for x in range(9)] for y in range(9)]
        self.assertEqual(is_valid(board), False)
