from game_of_life import get_neighbors
from hypothesis import given
from hypothesis.strategies import integers


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