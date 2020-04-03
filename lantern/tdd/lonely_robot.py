class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        if self.x > self.asteroid.x:
            raise MissAsteroidError()

    def turn_left(self):
        left = {"E": "N", "N": "W", "W": "S", "S": "E"}
        self.direction = left.get(self.direction, "N")

    def turn_right(self):
        right = {"E": "S", "S": "W", "W": "N", "N": "E"}
        self.direction = right.get(self.direction, "N")

    def move_forward(self):
        forward = {
            "N": {self.position: (self.x, self.y + 1)},
            "E": {self.position: (self.x + 1, self.y)},
            "S": {self.position: (self.x, self.y - 1)},
            "W": {self.position: (self.x - 1, self.y)},
        }
        self.position = forward.get(self.direction)

    def move_backward(self):
        backward = {
            "N": {self.position: (self.x, self.y - 1)},
            "E": {self.position: (self.x - 1, self.y)},
            "S": {self.position: (self.x, self.y + 1)},
            "W": {self.position: (self.x + 1, self.y)},
        }
        self.position = backward.get(self.direction)

class MissAsteroidError(Exception):
    def __str__(self):
        return 'Robot missed the asteroid!'
