# duel.py - run a simulation of a chess tournaments and output the results

import chess
import chess.engine
import bot

STOCKFISH_PATH = "/home/matt/software/stockfish/stockfish_20090216_x64_bmi2"


def setup():
    board = chess.Board()
    demo_game(board)
    print("Game Over")


def demo_game(board):
    """Run a test game with the stockfish engine playing against itself

    args:
        board: board to play on
    """
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

    while not board.is_game_over():
        bot.bot_fighting_fish(board, engine, 0.1)
        print(board)
        print()

    engine.quit


if __name__ == "__main__":
    setup()
    print(0)
