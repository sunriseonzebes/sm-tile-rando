class TRMapGrid:
    def __init__(self, width=1, height=1):
        self._squares = [[None for row in range(height)] for col in range(width)]

    def __getitem__(self, item):
        return self._squares[item]