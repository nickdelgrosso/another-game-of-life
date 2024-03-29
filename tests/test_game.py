from hypothesis import given
from hypothesis.strategies import integers
from game_of_life.domain import get_neighbors, count_live_neighbors, Board, Cell, create_board, should_flip_cell, BoardView, view_board
from pytest import fixture


@fixture
def view() -> BoardView:
    view: BoardView = [[True,  False, False, False, False],
                       [False, True,  True,  False, True],
                       [True,  True,  False, False, True],
                       [True,  False, True,  False, False]]
    return view


@fixture
def board(view):
    board: Board = {}
    for yi, line in enumerate(view):
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


def test_if_flip_rules_are_correct(board):
    assert should_flip_cell(board=board, cell=(0, 0))
    assert should_flip_cell(board=board, cell=(1, 0))
    assert not should_flip_cell(board=board, cell=(2, 0))
    assert not should_flip_cell(board=board, cell=(3, 0))
    assert not should_flip_cell(board=board, cell=(0, 2))
    assert not should_flip_cell(board=board, cell=(0, 3))
    assert should_flip_cell(board=board, cell=(2, 3))
    assert not should_flip_cell(board=board, cell=(2, 2))



def test_board_view(view, board):
    assert view_board(board) == view