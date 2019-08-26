import pyxel as px
from domain import run_game


width = 40
height = 40
seed = None
perc = 0.4

game = run_game(width=width, height=height, seed=seed, perc=perc)
board = next(game)

px.init(width=width, height=height, caption="Conway's Game of Life", fps=6)

def draw():
    for y, line in enumerate(board):
        for x, is_alive in enumerate(line):
            px.pix(x=x, y=y, col=7 if is_alive else 0)


def update():
    global board, game
    board = next(game)


px.run(update=update, draw=draw)