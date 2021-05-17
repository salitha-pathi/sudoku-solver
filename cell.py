class Cell:
    def __init__(self, x_pos: int, y_pos: int, initial_value: int):
        self.possibilities = []
        self.x_pos = x_pos
        self.y_pos = y_pos
        if 1 <= int(initial_value) <= 9:
            self.value = initial_value
            self.is_solved = True
        else:
            self.is_solved = False
            self.value = 0

    def set(self, possibilities: list):
        if len(possibilities) == 1:
            self.value = possibilities[0]
            self.is_solved = True
        else:
            self.possibilities = possibilities

    def __str__(self):
        if self.is_solved:
            return str(self.value)
        else:
            return f'({",".join(str(x) for x in self.possibilities)})'
