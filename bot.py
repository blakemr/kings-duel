# bot.py - A primitive chess bot

import chess
import random


def bot_basic(board):
    """Makes random moves

    args:
        board: chess.board handle
    """
    moves = list(board.legal_moves)
    selection = random.randrange(0, len(moves) - 1)
    board.push(moves[selection])


def bot_fighting_fish(board, engine, timelimit):
    """Uses an engine to compute moves

    args:
        board: chess.board handle
        engine: chess.engine handle
        timelimit: how much time the engine has to make a move (in seconds)

    """
    result = engine.play(board, chess.engine.Limit(timelimit))
    board.push(result.move)


if __name__ == "__main__":
    print("bot.py: Nothing to run.")
