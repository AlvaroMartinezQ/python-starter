class Matrix:

    def __init__(self, row, col, value=0):
        self.row=row
        self.col=col
        # _rows is a protected attribute
        # _ indicates that value is not important could be replaced with an i
        self._rows=[[value] * col for _ in range(row)] 

    def size(self):
        return self.row*self.col

    
