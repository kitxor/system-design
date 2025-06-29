from board import Board
from game import Game
from player import Player

if __name__ == "__main__":
    player1 = Player("Mahesh")
    player2 = Player("Alex Ravi")

    snake_config = {
        16: 6,  # Early snake
        47: 26,  # Mid-game snake
        49: 11,  # Another mid snake
        56: 53,  # Small snake
        62: 19,  # Big drop
        64: 60,  # Small snake
        87: 24,  # Late game punisher
        93: 73,  # Another big one
        95: 75,  # Near-end snake
        98: 78  # Brutal near-win snake
    }

    ladder_config = {
        2: 38,  # Early boost
        7: 14,  # Small ladder
        8: 31,  # Good early ladder
        15: 26,  # Mid ladder
        21: 42,  # Nice jump
        28: 84,  # HUGE ladder (game changer)
        36: 44,  # Small ladder
        51: 67,  # Mid-game boost
        71: 91,  # Late game ladder
        78: 98  # Near-end ladder (but watch out for snake at 98!)
    }

    board = Board(snake_config, ladder_config)
    game = Game([player1, player2], board)
    game.start()
