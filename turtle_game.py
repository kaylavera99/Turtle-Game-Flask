# turtle_game.py
class TurtleGame:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.score = 0

    def move_up(self):
        self.y += 1
        self.score += 1  # Increment score for moving up
        return {"x": self.x, "y": self.y, "score": self.score}

    def move_down(self):
        self.y -= 1
        self.score += 1  # Increment score for moving down
        return {"x": self.x, "y": self.y, "score": self.score}

    def move_left(self):
        self.x -= 1
        self.score += 1  # Increment score for moving left
        return {"x": self.x, "y": self.y, "score": self.score}

    def move_right(self):
        self.x += 1
        self.score += 1  # Increment score for moving right
        return {"x": self.x, "y": self.y, "score": self.score}

game = TurtleGame()
