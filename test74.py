class MortalCoil:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[False] * width for _ in range(height)]
        self.visited = set()
        self.current_position = (height // 2, width // 2)

    def move(self, direction):
        x, y = self.current_position
        dx, dy = direction
        steps = 0
        while 0 <= x + dx < self.height and 0 <= y + dy < self.width:
            x += dx
            y += dy
            steps += 1
            if self.grid[x][y] or (x, y) in self.visited:
                break
        for _ in range(steps):
            self.grid[self.current_position[0]][self.current_position[1]] = True
            self.visited.add(self.current_position)
            self.current_position = (self.current_position[0] + direction[0],
                                     self.current_position[1] + direction[1])

    def print_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self.current_position:
                    print("X", end=" ")
                elif self.grid[i][j]:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            print()

    def fill_grid(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        while len(self.visited) < self.width * self.height:
            for direction in directions:
                self.move(direction)

if __name__ == "__main__":
    width = 10
    height = 10
    game = MortalCoil(width, height)
    game.fill_grid()
    game.print_grid()
