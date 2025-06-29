import time


class Game:
    """
    game has players and board.
    1. starts  the game
    2. manages turn
    3. asks player whose turn it is to roll dice
    4. asks board the position
    5. checks winner at each position movement
    6. if someone wins -> ends game or keeps going

    """

    def __init__(self, players, board):
        """
        composition over construction.
        game receives ready - made dependencies (players and board)
        this is dependency injection
        vs
        game creates its own dependencies (factory pattern), dependency injection is cleaner

        """
        self.players = players
        self.board = board
        self.current_player_index = 0  # start with 0

    def check_winner(self, position):
        if position == 100:
            return True
        return False

    def start(self):
        keep_playing = True
        print("start play: \n")
        while keep_playing:
            # start the game
            turn = self.current_player_index
            # get player
            player = self.players[turn]
            # get dice result
            dice_result = player.roll_dice()
            print(f"player: {player.name} rolled {dice_result}")
            # move position
            current_pos = player.position
            tentative_new_pos = current_pos + dice_result
            print(f"their current position is {current_pos} and tentative new position is {tentative_new_pos}")
            if tentative_new_pos > 100:
                # stay where you are
                final_pos = current_pos
                print(f"but tentative position > 100 so stay put at {current_pos}")
            else:
                # ask board for final position
                final_pos = self.board.get_new_position(tentative_new_pos)
                print(f"hmm, board says move to {final_pos}")
            player.set_position(final_pos)
            # check winner
            if self.check_winner(final_pos) is True:
                # end game
                keep_playing = False
                print(f"damn man, {player.name} wins!")
            else:
                self.current_player_index = (self.current_player_index + 1) % len(self.players)
                print(f"End of turn for {player.name} ")
                time.sleep(2)
