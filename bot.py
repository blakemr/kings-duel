# bot.py - Interfaces to various chess bots

import chess
import random
from queue import PriorityQueue


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


def bot_timeout_search(board, timelimit):
    """Search for a move until the time limit runs out

    args:
        board: chess.board handle
        timelimit: how much time the engine has to make a move (in seconds)
    """
    move_queue = PriorityQueue()

    # TODO:
    #   * Set up a timeout exception
    #   * Loop until timeout
    #   * Set up a priority queue with the best moves
    #   * Factors include, piece advantage, position, castling
    #   * On timeout, return the highest priority move
    #
    # For the timing, signal seems to be the correct package,
    # but it has a different api if you're using Windows, so this function
    # should take care of that as well.
    board.push(move_queue.get())


if __name__ == "__main__":
    print("bot.py: Nothing to run.")
