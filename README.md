[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11387145&assignment_repo_type=AssignmentRepo)
# Python Sudoku Solver

O script principal de vocês deve estar no arquivo `main.py`.

## 📝 Instruções 📝

Nesse script, voce irá implementar duas funções que resolvem um tabuleiro de [Sudoku](https://pt.wikipedia.org/wiki/Sudoku) na versão 9x9.

A função `solve_sudoku` recebe um tabuleiro de Sudoku incompleto e retorna o tabuleiro completo.
Caso seja impossível completar o tabuleiro passado, a função deve lançar uma exceção do tipo `ValueError` com a mensagem `Sudoku impossível de resolver`.

A função `is_valid` recebe um tabuleiro de Sudoku e verifica se ele é válido retornando `False` caso ele seja inválido e `True` quando ele é válido.
Um tabuleiro de Sudoku é válido se ele não viola nenhuma das regras do jogo.

As regras são as seguintes:

1. Cada linha deve conter os números de 1 a 9 sem repetição.
2. Cada coluna deve conter os números de 1 a 9 sem repetição.
3. Temos 9 subgrid 3x3 que devem conter os números de 1 a 9 sem repetição.
4. Cada célula deve conter um número de 1 a 9 ou estar vazia.

Para facilitar a implementação, assuma que `0` em uma célula representa uma célula vazia.
Também, assuma que o tabuleiro de Sudoku é uma lista de listas de inteiros.
Ou seja, um tabuleiro de Sudoku é uma lista de 9 listas de 9 inteiros.

Um exemplo de Sudoku válido, mas ainda incompleto, é o seguinte:

```python
sudoku_board = [
   [5, 3, 0, 0, 7, 0, 0, 0, 0],
   [6, 0, 0, 1, 9, 5, 0, 0, 0],
   [0, 9, 8, 0, 0, 0, 0, 6, 0],
   [8, 0, 0, 0, 6, 0, 0, 0, 3],
   [4, 0, 0, 8, 0, 3, 0, 0, 1],
   [7, 0, 0, 0, 2, 0, 0, 0, 6],
   [0, 6, 0, 0, 0, 0, 2, 8, 0],
   [0, 0, 0, 4, 1, 9, 0, 0, 5],
   [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

## 🧑‍💻 Exemplo de Execução 🧑‍💻

```python
>>> sudoku_board = [
   [5, 3, 0, 0, 7, 0, 0, 0, 0],
   [6, 0, 0, 1, 9, 5, 0, 0, 0],
   [0, 9, 8, 0, 0, 0, 0, 6, 0],
   [8, 0, 0, 0, 6, 0, 0, 0, 3],
   [4, 0, 0, 8, 0, 3, 0, 0, 1],
   [7, 0, 0, 0, 2, 0, 0, 0, 6],
   [0, 6, 0, 0, 0, 0, 2, 8, 0],
   [0, 0, 0, 4, 1, 9, 0, 0, 5],
   [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
>>> is_valid(sudoku_board)
True
>>> solved_board = solve_sudoku(sudoku_board)
>>> is_valid(solved_board)
True
>>> solved_board
[
   [5, 3, 4, 6, 7, 8, 9, 1, 2],
   [6, 7, 2, 1, 9, 5, 3, 4, 8],
   [1, 9, 8, 3, 4, 2, 5, 6, 7],
   [8, 5, 9, 7, 6, 1, 4, 2, 3],
   [4, 2, 6, 8, 5, 3, 7, 9, 1],
   [7, 1, 3, 9, 2, 4, 8, 5, 6],
   [9, 6, 1, 5, 3, 7, 2, 8, 4],
   [2, 8, 7, 4, 1, 9, 6, 3, 5],
   [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
```

## ❗ IMPORTANTE ❗

Veja as instruções sobre como proceder com o exercício no link [Instruções Gerais Para os Exercícios](https://github.com/ProfRonan/python-exercise-instructions).
