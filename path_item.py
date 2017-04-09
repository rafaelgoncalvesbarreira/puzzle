class PathItem:
    """ """
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent

    # def equals(self, other):
    #     return self.item.equals(other.item)
    def equals(self, other):
        #return self.calculate_equals(other) == self.size
        return self.board==other.board

    def calculate_equals(self, target):
        same = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == target.board[i][j]:
                    same += 1
        return same

    def calc_G(self):
        count = 0
        cursor = self.parent
        while cursor != None:
            count = count +1
            cursor = cursor.parent

        return count

    def calc_H(self, target):
        size = len(self.board) * len(self.board[0])
        H = (size - self.calculate_equals(target))
        return H

    def recalculate_cost(self, target):
        self.costF = self.calculate_cost(target)
    def calculate_cost(self, target):
        '''
        F = G + H
        '''
        return self.calc_G() + self.calc_H(target)
    
    
    def swap_zero(self, zero_row, zero_col, row, col):
        import copy
        copied = copy.deepcopy( self.board)
        copied[zero_row][zero_col] = copied[row][col]
        copied[row][col] = 0

        return copied

    def get_adjacent(self):
        adjacents = []
        row = 0
        col = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    row = i
                    col = j

        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if (r== row) != (c == col):
                    if (0 <= r < 3) and (0 <= c < 3):
                        adjacents.append(PathItem(self.swap_zero(row, col, r, c), self))

        return adjacents
