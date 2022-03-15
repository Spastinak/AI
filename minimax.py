class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Choice():
    def __init__(self, move, value):
        self.move = move
        self.value = value

    def __str__(self) -> str:
        return self.move + ": " + str(self.value)
        