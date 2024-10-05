from board import Board
from utils import raiseNotDefined

def minimax(board, depth, maximizing_player, player_color,use_pruning=False,alpha = -float('inf'),beta = float('inf')):
    """
    Implements the Minimax algorithm to determine the best move for a player in an Othello game.

    Args:
        board (Board): The current game board.
        depth (int): The remaining depth to search in the game tree.
        maximizing_player (bool): A boolean indicating whether the current player is the maximizing player.
        player_color (str): The color of the current player ('B' for black, 'W' for white).

    Returns:
        tuple: A tuple containing the best move (row, col) and its evaluation score (int). 
               If no valid moves are available, returns (None, evaluation score).
    """
    
    
    raiseNotDefined()

def evaluate_board(board, player_color):
    """
    Evaluates the current board state for a given player by comparing the scores.

    Args:
        board (Board): The current game board.
        player_color (str): The color of the player to evaluate the score for ('B' for black, 'W' for white).

    Returns:
        int: The difference between the player's score and the opponent's score.
             A positive value favors the player, and a negative value favors the opponent.
    """
    #improve the evaluation function 
    
    B_score, W_score = board.get_score()
    if player_color == 'white':
        return W_score - B_score
    else:
        return B_score - W_score


def copy_board(board):
    """
    Creates a deep copy of the current board to simulate future moves without altering the original.

    Args:
        board (Board): The current game board to be copied.

    Returns:
        Board: A new Board object with the same state as the original.
    """
    new_board = Board(board.size)
    new_board.board = [row[:] for row in board.board]
    return new_board