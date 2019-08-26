from game_of_life import get_neighbors

def test_neighbors():
    x, y = 2, 3
    cell = (x, y)

    for idx, neighbor in enumerate(get_neighbors(cell)):
        assert neighbor in [
            (x + 1, y + 1), (x + 1, y), (x + 1, y - 1),
            (x    , y + 1),             (x    , y - 1),
            (x - 1, y + 1), (x - 1, y), (x - 1, y - 1),
        ]
        assert neighbor != cell
    assert idx == 7