class Matrix:

    def __init__(self, row, col, value=0):
        self.row=row
        self.col=col
        # _rows is a protected attribute
        # _ indicates that value is not important could be replaced with an i
        self._rows=[[value] * col for _ in range(row)] 

    def size(self):
        return self.row*self.col

    def __getitem__(self, idx):
        return self._rows[idx]
        
    def __setitem__(self, idx, item):
        self._rows[idx] = item

    def __str__(self):
        s = '\n'.join([ ' '.join([ str(item) for item in row]) for row in self ._rows])
        return s

    def transpose(self):
        self.row, self.col = self.col, self.row
        self ._rows = [ list (item) for item in zip(*self ._rows)]

    def get_rank(self):
        return self.row, self.col

    def __eq__(self, mat):
        return self._rows == mat._rows

    def __add__(self, mat):
        if self.get_rank() != mat.get_rank():
            raise Exception("Matrixes rank aren't equal and won't be added.")

        ret = Matrix(self.row, self.col)

        for x in range(self.row):
            row = [sum(item) for item in zip(self ._rows[x], mat[x])]
            ret[x] = row
        
        return ret 

    def __sub__ (self , mat):
        if self .get_rank() != mat.get_rank():
            raise Exception ("Matrixes rank aren't equal and won't be substracted.")
        
        ret = Matrix(self.row, self.col)

        for x in range(self.row):
            row = [item[0] - item[1] for item in zip(self ._rows[x], mat[x])]
            ret[x] = row
        
        return ret

    def __iadd__ (self , mat):
        temp_mat = self + mat
        self ._rows = temp_mat._rows[:]
        return self
 
    def __isub__ (self , mat):
        temp_mat = self - mat
        self ._rows = temp_mat._rows[:]
        return self
