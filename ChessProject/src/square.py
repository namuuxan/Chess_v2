class Square:
    ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.alphacol = self.ALPHACOLS[col]

    def __str__(self):
        return f'({self.row}, {self.col})'

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def has_piece(self):
        return self.piece is not None

    def has_team_piece(self, color):
        return self.piece is not None and self.piece.color == color

    def has_rival_piece(self, color):
        return self.piece is not None and self.piece.color != color
    
    def isempty(self):
        return self.piece is None

    def isempty_or_rival(self, color):
        return self.piece is None or self.piece.color != color

    @staticmethod
    def in_range(*args):
        return all(0 <= arg < 8 for arg in args)

    @staticmethod
    def get_alphacol(col):
        return Square.ALPHACOLS[col]
