class Ladder:
    def __init__(self, jump_config):
        self.jump = jump_config

    def found_a_ladder(self, position):
        if position in self.jump:
            return self.jump[position]
        else:
            return None
