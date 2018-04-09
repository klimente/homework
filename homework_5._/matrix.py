"""Matrix"""

from functools import reduce, wraps
from operator import add, mul, eq, sub


class Matrix:
    """Class representing matrix and some basic operations.
    """
    class Decorators:
        """Class of decorators for functions in Matrix.
        """
        @classmethod
        def matrix_cheker(cls, func):
            """Decorator to verify argument for basic math operations.

            :param func: function of math operation.
            :param func: function.
            :returns: function -- decorated function.
            :raises: TypeError.
            """
            print(cls)
            @wraps(func)
            def inner(*args):
                """Service function"""
                if not isinstance(args[1], Matrix):
                    raise TypeError(f"Cannot execute action to type {type(args[1])}")
                return func(*args)
            return inner

        @classmethod
        def int_cheker(cls, func):
            """Decorator to verify argument to int and deliver in function.

            :param func: decorated function.
            :param func: function.
            :returns: decorated function.
            :raises: ValueError.
            """
            @wraps(func)
            def inner(*args):
                """Service function"""
                if not isinstance(args[1], int):
                    raise ValueError("Index must be int")
                return func(*args)
            return inner

        @classmethod
        def equal_size_cheker(cls, func):
            """Decorator to check size of two matrix.

            :param func: function that needs check size of matrix.
            :param func: function.
            :returns: function -- decorated functions.
            :raises: ValueError.
            """
            @wraps(func)
            def inner(*args):
                """Service function"""
                if not (args[0].row == args[1].row and args[0].column == args[1].column):
                    raise ValueError("Size of both matrix must be equal")
                return func(*args)
            return inner

    def __init__(self, *args):
        """Creates instance of matrix.

        :param args: positional arg: can take 2: arg[0] amount of rows, arg[1] amount of columns, or matrix itself.
        :param args: int or list.
        :returns: instance of matrix.
        :raises: TypeError,ValueError.
        """
        if len(args) == 1 and isinstance(args[0], list):
            for row in args[0]:
                if not isinstance(row, list):
                    raise TypeError("Element of matrix must be list")
                if not len(args[0][0]) == len(row):
                    raise ValueError("Matrix is not rectangle or square")
                if not all(map(lambda x: isinstance(x, int), row)):
                    raise TypeError("Elements of matrix must be int")
            self.row = len(args[0])
            self.column = len(args[0][0])
            self.matrix = args[0]
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            if args[0] < 0 or args[1] < 0:
                raise ValueError("Row or column is not correct")
            self.row = args[0]
            self.column = args[1]
            self.matrix = [[x for x in range(self.column)] for _ in range(self.row)]
        else:
            raise TypeError("Arguments is not correct")

    @Decorators.int_cheker
    def get_col(self, index):
        """A method to get a column.

        :param index: number of columns.
        :param index: int.
        :returns: one column.
        :raises: ValueError.
        """
        if index < 0 or index > self.column:
            raise ValueError("Index must be in range of matrix column")
        return [row[index] for row in self.matrix]

    @Decorators.int_cheker
    def get_row(self, index):
        """A method to get a row.

        :param index: number of rows.
        :param index: int.
        :returns: one row.
        :raises: ValueError.
        """
        if index < 0 or index > self.row:
            raise ValueError("Index must be in range of matrix row")
        return self.matrix[index]

    def transpose(self):
        """A method to transpose matrix and return new one.

        :returns: Matrix -- Transpose matrix.
        """
        return Matrix([self.get_col(col) for col in range(self.column)])

    def __str__(self):
        """Representation matrix.
        """
        return '[' + '\n'.join([f"{row}" for row in self.matrix]) + ']'

    @Decorators.matrix_cheker
    @Decorators.equal_size_cheker
    def __add__(self, other):
        """A method to add matrix to a other one.

        :param other: other matrix to add to self.
        :param other: Matrix.
        :returns: Matrix -- Result of addition.
        """
        result = []
        for row in range(self.row):
            result.append(list(map(add, self.matrix[row], other.matrix[row])))
        return Matrix(result)

    @Decorators.matrix_cheker
    @Decorators.equal_size_cheker
    def __sub__(self, other):
        """A method to subtract from this matrix other one.

        :param other: other matrix to subtract from self.
        :param other: Matrix.
        :returns: Matrix -- Result of subtract.
        """
        result = []
        for row in range(self.row):
            result.append(list(map(sub, self.matrix[row], other.matrix[row])))
        return Matrix(result)

    def is_square(self):
        """A method to check Matrix is that square matrix.

        :returns: bool -- answer
        """
        return self.row == self.column

    @Decorators.matrix_cheker
    def __eq__(self, other):
        """A method to verify the equivalence of two matrix.

         :param other: comparable matrix
         :param other: Matrix
         :returns: bool -- result
         """
        res = []
        for row in range(self.row):
            res.append(all(list(map(eq, self.matrix[row], other.matrix[row]))))
        return all(res)

    @Decorators.matrix_cheker
    def __mul__(self, other):
        """A method to multiply two matrices.

        :param other: Matrix to multiply.
        :param other: Matrix.
        :returns: Matrix -- result of multiplying.
        :raises: ValueError
         """
        if not self.column == other.row:
            raise ValueError("Columns are not equal to rows")
        result = []
        for row in range(self.row):
            result.append([reduce(add, map(mul, self.matrix[row], other.get_col(x))) for x in range(other.column)])
        return Matrix(result)

    @Decorators.int_cheker
    def __rmul__(self, other):
        """A method to multiply scalar on matrix.

        :param other: scalar.
        :param other: int.
        :returns: Matrix -- result.
        """
        return Matrix([list(map(lambda x: x*other, row)) for row in self.matrix])

    def is_symmetric(self):
        """A method to check squere matrix is that symmetric.

         :returns: bool -- result.
         :raises: TypeError.
         """
        if not self.is_square():
            raise TypeError("This is not square matrix")
        return self == self.transpose()

if __name__ == "__main__":
    A = Matrix([[1, 2, 3, 4], [1, 2, 3, 4]])
    B = Matrix(2, 4)
    F = Matrix(2, 4)
    print(f"Матрица А :\n{A}")
    print(f"Матрица B :\n{B}")
    print(f"Сложение матриц А и B:\n{A + B}") #1
    print(f"Разница матриц А и B:\n {A - B}") #2
    C = Matrix([[1], [2], [3], [4]])
    print(f"Матрица C :\n{C}")
    print(f"Умножение матрицы А на С :\n{A * C}") #3
    print(f"Умножение скаляра 3 на матрицу А:\n{3 * A}") #4
    D = Matrix([[1, 2, 3], [2, 1, 2], [3, 2, 1]])
    print(f"Матрица B :\n{D}")
    print(f"Квадратна ли матрица D:\n{D.is_square()}\n квадртна ли матрица А:\n{A.is_square()}") #5
    print(f"Симметрична ли матрица D относительно диаганали :\n{D.is_symmetric()}") #6
    print(f"Транспонированная матрица А:\n{A.transpose()}") #7
    print(f"Равна ли матрица А матрице B:\n{A == B}") #8
    print(B == F)
    #raises exceprion
    #print(A + "s")
    #print(A + B)
    #print(A * B)
    #Matrix(1,2,3)
    #Matrix([[1,2,3],(1,2,3)])
    #Matrix([[1.2,2],[1,2]])
    #Matrix()
    #Matrix([[1,2,3],[1,2]])
    #A.is_symmetrix
