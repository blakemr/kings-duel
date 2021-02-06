# duel.py - run a simulation of a chess tournaments and output the results
#
# Takes in an argument for the path of the engine you want to use.
# If no argument is given, each player will make random moves

import sys
import chess
import chess.engine
import bot


def setup():
    """Sets up the game

    returns:
        chessboard handle
    """
    board = chess.Board()
    return board


def engine_game(board, engine_path):
    """Run a game with a chess engine playing against itself

    args:
        board: board to play on
        engine_path: path to engine to be used
    """
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)

    while not board.is_game_over():
        bot.bot_fighting_fish(board, engine, 0.1)

        print(board)
        print()

    engine.quit


def random_game(board):
    """Run a game with each player making random moves

    args:
        board: board to play on

    """
    while not board.is_game_over():
        bot.bot_basic(board)

        print(board)
        print()


if __name__ == "__main__":
    engine_path = sys.argv[1]

    board = setup()

    if not engine_path:
        random_game(board)

    else:
        engine_game(board, engine_path)

    print(0)
