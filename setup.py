from setuptools import setup


setup(
    name='game_of_life',
    version='0.1',
    packages=["game_of_life"],
    url='',
    license='',
    author='NickDG',
    author_email='',
    install_requires=['pyxel'],
    description="Simple Conway's Game of Life implementation, rendered with Pyxel.",
    entry_points={
        'console_scripts': ['agol=game_of_life.app:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)





