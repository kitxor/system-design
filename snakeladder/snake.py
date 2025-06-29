class Snake:
    def __init__(self, jump_config):
        self.jump = jump_config

    def bit_by_snake(self, position):
        if position in self.jump:
            return self.jump[position]
        else:
            return None
