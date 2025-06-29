from random import randint


class Player:
    """
    Player has just one job:
    roll the dice
    """

    def __init__(self, name):
        self.name = name
        self.position = 1  # start at position 1

    def roll_dice(self):
        return randint(1, 6)

    def set_position(self, new_position):
        self.position = new_position
