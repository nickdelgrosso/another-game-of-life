from typing import NewType, Dict, Tuple, List, Generator, Iterable
from itertools import product

Cell = Tuple[int, int]
Board = NewType("LifeBoard", Dict[Cell, bool])


def get_neighbors(cell: Cell) -> Iterable[Cell]:
    """Get all neighbors of the cell."""
    x, y = cell
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        if not all([dx == 0, dy == 0]):
            neighbor: Cell = (x + dx, y + dy)
            yield neighbor


def create_board(width=10, height=10):
    board: Board = {(x, y): False for x, y in product(list(range(width)), list(range(height)))}
    return board


def count_live_neighbors(cell: Cell, board: Board) -> int:
    return sum(board.get(neighbor, False) for neighbor in get_neighbors(cell=cell))


def is_alive(cell: Cell, board: Board) -> bool:
    return board[cell]


def should_flip_cell(cell: Cell, board: Board) -> bool:
    """
    Implement neighbor rules to say whether cell should flip.

    Source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules
    """
    n_neighbors = count_live_neighbors(cell=cell, board=board)
    if is_alive(cell=cell, board=board):
        return False if 1 < n_neighbors < 4 else True
    else:
        return True if n_neighbors == 3 else False


def update_board(board: Board) -> Board:
    new_board: Board = {cell: not should_flip_cell(cell, board) for cell in board}
    return new_board


BoardView = NewType("BoardView", List[List[bool]])
def view_board(board: Board) -> BoardView:
    width = max(board, key=lambda x: x[0])[0] + 1
    height = max(board, key=lambda x: x[1])[1] + 1
    view: BoardView = [[board[(x, y)] for x in range(width)] for y in range(height)]
    return view




