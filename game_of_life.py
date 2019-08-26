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

