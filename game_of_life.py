from typing import NewType, Dict, Tuple, List, Generator, Iterable
from itertools import product

Cell = Tuple[int, int]
Board = NewType("Board", Dict[Cell, bool])


def get_neighbors(cell: Cell) -> Iterable[Cell]:
    x, y = cell
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        if not all([dx == 0, dy == 0]):
            neighbor: Cell = (x + dx, y + dy)
            yield neighbor








