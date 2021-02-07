# bot.py - Interfaces to various chess bots

import chess
import random


def bot_random(board):
    """A bot that only makes random moves

    args:
        board: chess.board handle
    """
    move = random.choice(list(board.legal_moves))
    board.push(move)


def bot_engine(board, engine, timelimit):
    """Use an engine to compute moves

    args:
        board: chess.board handle
        engine: chess.engine handle
        timelimit: how much time the engine has to make a move (in seconds)

    """
    result = engine.play(board, chess.engine.Limit(timelimit))
    board.push(result.move)


if __name__ == "__main__":
    print("bot.py: Nothing to run.")
