from hypothesis import given
from hypothesis.strategies import integers
from game_of_life import get_neighbors, count_live_neighbors, Board, Cell, create_board
from pytest import fixture


@fixture
def board() -> Board:
    orig_board = [[True,  False, False, False, False],
                  [False, True,  True,  False, True],
                  [True,  True,  False, False, True],
                  [True,  False, True,  False, False]]
    board: Board = {}
    for yi, line in enumerate(orig_board):
        for xi, cell in enumerate(line):
            loc: Cell = (xi, yi)
            board[loc] = cell
    return board


@given(integers(), integers())
def test_neighbors(x, y):
    cell = (x, y)

    for idx, neighbor in enumerate(get_neighbors(cell)):
        assert neighbor in [
            (x + 1, y + 1), (x + 1, y), (x + 1, y - 1),
            (x    , y + 1),             (x    , y - 1),
            (x - 1, y + 1), (x - 1, y), (x - 1, y - 1),
        ]
        assert neighbor != cell
    assert idx == 7


@given(integers(min_value=0, max_value=200), integers(min_value=0, max_value=200))
def test_board_creation(width, height):
    assert len(create_board(width=width, height=height)) == width * height


def test_neighbor_live_count(board):
    assert count_live_neighbors(board=board, cell=(1, 1)) == 4
    assert count_live_neighbors(board=board, cell=(2, 2)) == 4
    assert count_live_neighbors(board=board, cell=(0, 0)) == 1
    assert count_live_neighbors(board=board, cell=(2, 3)) == 1
    assert count_live_neighbors(board=board, cell=(3, 2)) == 4


def test_neighboar_count_on_board_fringe_still_works(board):
    assert count_live_neighbors(board=board, cell=(-1, -1)) == 1
    assert count_live_neighbors(board=board, cell=(-1, 2)) == 2


def test_neighbor_count_beyond_board_is_0(board):
    assert count_live_neighbors(board=board, cell=(10, 10)) == 0
    assert count_live_neighbors(board=board, cell=(-2, -2)) == 0

