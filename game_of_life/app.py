from typing import Optional
from abc import ABCMeta
import pyxel as px
from . import run_game


class BaseApp(metaclass=ABCMeta):

    def __init__(self, width: int = 100, height: int = 100, seed: Optional[int] = None, perc: float = 0.3):
        self.width = width
        self.height = height
        self.seed = seed
        self.perc = perc

        self.game = run_game(width=width, height=height, seed=seed, perc=perc)
        self.board = next(self.game)
        self.init()

    def init(self):
        """Initialization function (optional."""
        pass

    def check_if_restart(self) -> bool:
        """Overrridable callable function for checking whether restart is needed.  Will be called by App.update()"""
        pass

    def update(self):
        self.board = next(self.game)
        if self.check_if_restart():
            self.game = run_game(width=self.width, height=self.height, seed=self.seed, perc=self.perc)

    def run(self):
        """Overridable callable function for running main loop."""


class PyxelApp(BaseApp):

    def init(self):
        px.init(width=self.width, height=self.height, caption="Conway's Game of Life (space to restart, escape to exit)", fps=8)

    def check_if_restart(self):
        return px.btn(px.KEY_SPACE)

    def draw(self):
        for y, line in enumerate(self.board):
            for x, is_alive in enumerate(line):
                px.pix(x=x, y=y, col=7 if is_alive else 0)

    def run(self):
        px.run(update=self.update, draw=self.draw)


def main():
    app = PyxelApp()
    app.run()
