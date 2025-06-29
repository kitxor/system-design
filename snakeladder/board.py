from ladder import Ladder
from snake import Snake


class Board:
    def __init__(self, snake_config, ladder_config):
        self.snake = Snake(snake_config)
        self.ladder = Ladder(ladder_config)

    def get_new_position(self, position):
        snake_result = self.snake.bit_by_snake(position)
        if snake_result is not None:
            position = snake_result

        ladder_result = self.ladder.found_a_ladder(position)
        if ladder_result is not None:
            position = ladder_result

        return position
