from Sudoku import Sudoku

Game = Sudoku([[1, 2, 0, 0, 7, 0, 5, 6, 0],
               [5, 0, 7, 9, 3, 2, 0, 8, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0],
               [0, 1, 0, 2, 4, 0, 0, 5, 0],
               [3, 0, 8, 0, 0, 0, 4, 0, 2],
               [0, 7, 0, 0, 8, 5, 0, 1, 0],
               [0, 0, 0, 7, 0, 0, 0, 0, 0],
               [0, 8, 0, 4, 2, 3, 7, 0, 1],
               [0, 3, 4, 0, 1, 0, 0, 2, 8]]
              )

Game = Sudoku([[0, 0, 0, 7, 0, 0, 0, 4, 0],
               [0, 2, 0, 8, 0, 1, 9, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 7, 3],
               [1, 0, 2, 0, 0, 6, 0, 9, 7],
               [6, 0, 0, 0, 9, 0, 0, 0, 1],
               [9, 7, 0, 1, 0, 0, 4, 0, 5],
               [3, 5, 4, 0, 0, 0, 0, 0, 0],
               [0, 0, 8, 6, 0, 4, 0, 3, 0],
               [0, 1, 0, 0, 0, 3, 0, 0, 0]]
              )

Game = Sudoku([[0, 9, 0, 0, 0, 2, 0, 0, 0],
               [0, 0, 0, 7, 0, 0, 0, 0, 0],
               [7, 0, 0, 1, 0, 0, 2, 0, 4],
               [9, 0, 2, 0, 0, 0, 0, 1, 5],
               [0, 8, 0, 0, 0, 0, 7, 6, 0],
               [0, 0, 4, 0, 6, 0, 0, 0, 0],
               [0, 0, 1, 9, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 5, 0, 8, 3, 0],
               [0, 0, 0, 6, 0, 0, 0, 0, 9]]
              )

Game = Sudoku([[0, 0, 6, 0, 0, 0, 0, 5, 0],
               [0, 0, 3, 7, 0, 0, 0, 0, 0],
               [7, 0, 0, 0, 3, 5, 0, 0, 8],
               [0, 0, 0, 0, 7, 0, 0, 1, 2],
               [0, 0, 0, 9, 4, 2, 0, 0, 0],
               [6, 2, 0, 0, 8, 0, 0, 0, 0],
               [9, 0, 0, 1, 2, 0, 0, 0, 3],
               [0, 0, 0, 0, 0, 3, 6, 0, 0],
               [0, 5, 0, 0, 0, 0, 7, 0, 0]]
              )

print(Game)
while not Game.finished():
    Game.calculate_possibilities()
    Game.global_depression()
    Game.calculate_possibilities()
    Game.global_uniqueness()
print(Game)