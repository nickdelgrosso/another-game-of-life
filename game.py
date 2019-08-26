from typing import NewType, Dict, Tuple, List, Generator, Iterable, Optional
from itertools import product
import random
import pyxel as px

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


def seed_board(board: Board, seed: Optional[int] = None, perc: float = 0.2) -> Board:
    """adds a percentage of living cells to an existing board."""
    if not 0. <= perc <= 1.:
        raise ValueError("percentage should be between 0 and 1.")
    if seed is not None:
        random.seed(seed)
    new_board: Board = {cell: True if random.random() <= perc else is_alive for cell, is_alive in board.items()}
    return new_board


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


def run_game(width: int, height: int, seed: Optional[int] = None, perc: float = 0.4) -> Iterable[BoardView]:
    """Main Game of Life Function."""
    board = seed_board(create_board(width=width, height=height), seed=seed, perc=perc)
    while True:
        yield view_board(board)
        board = update_board(board=board)

