""" Test the game"""

from rock_paper_scissor import game


class Test_game(game):
    """This class is derived from parent game class"""
    game_try = game()
    game_try.lets_play()

