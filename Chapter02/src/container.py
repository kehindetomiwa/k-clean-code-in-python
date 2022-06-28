"""Chapter 2 - Containers"""


class Boundaries:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width=width, height=height)

    def __contains__(self, coord):
        return coord in self.limits


def mark_coordinate(grid, coord):
    if coord in grid:
        grid[coord] = "Marked"
