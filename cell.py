class Cell:
    def __init__(self, value, position):
        self.value = value
        self.neighbours = []
        self.position = position
        self.selected = False

    def value_in_neighbour(self):
        for cell in self.neighbours:
            if cell.value == self.value:
                return True

        return False

    def as_string(self):
        if self.value != 0:
            return str(self.value)
        return " "

    def __repr__(self):
        return str(self.position) + "  " + str(self.value)