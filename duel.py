# duel.py - run a simulation of a chess tournaments and output the results
#
# Takes in an argument for the path of the engine you want to use.

import sys
import chess
import chess.engine
import bot

STOCKFISH_PATH = "/home/matt/software/stockfish/stockfish_20090216_x64_bmi2"


def setup():
    """Sets up the game

    returns:
        chessboard handle
    """
    board = chess.Board()
    return board


def demo_game(board, engine_path):
    """Run a test game with a chess engine playing against itself

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


if __name__ == "__main__":
    engine_path = sys.argv[1]

    if not engine_path:
        NotImplemented

    board = setup()
    demo_game(board, engine_path)
