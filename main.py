class Circle:
    pi = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self) -> float:
        return self.pi * self.radius ** 2
