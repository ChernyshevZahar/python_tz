class Matric:

    def __init__(self,roll,col):
        self.col = col
        self.roll = roll
        self.data = [[0 for _ in range(col)] for _ in range(roll)]
        

    def add (self,other):
        if self.roll != other.roll or self.col != other.col:
            raise ValueError('размеры матрицы не совпадают')

        addData = Matric(self.roll,self.col)

        for i in range(self.roll):
            for j in range(self.col):
                addData.data[i][j] = self.data[i][j] + other.data[i][j]
        return addData
        

    def subtract (self,other):
        if self.col != other.col and self.roll != other.roll:
            raise ValueError('размеры матрицы не совпадают')

        addData = Matric(self.roll,self.col)

        for i in range(self.roll):
            for j in range(self.col):
                addData.data[i][j] = self.data[i][j] - other.data[i][j]

        return addData

    def multiply (self,other):
        if self.col != other.roll:
            raise ValueError('размеры матрицы не совпадают')

        addData = Matric(self.roll,self.col)

        for i in range(self.roll):
            for j in range(other.col):
                for g in range(self.col):
                    addData.data[i][j] += self.data[i][g] * other.data[g][j]

        return addData

    def transpose (self):
       

        addData = Matric(self.col,self.roll)

        for i in range(self.roll):
            for j in range(self.col):
                addData.data[j][i] = self.data[i][j]
        return addData

    def __str__(self):
    # Форматирование строк матрицы
        res = "\n".join(["\t".join(map(str, row)) for row in self.data])
        return res

if __name__ == "__main__":
    m1 = Matric(2,3)
    m1.data = [[1, 2, 3], [4, 5, 6]]
    m2 = Matric(2, 3)
    m2.data = [[7, 8, 9], [10, 11, 12]]
    # Тестирование операций
    print("Матрица 1:")
    print(m1)
    print("Матрица 2:")
    print(m2)
    print("Сложение матриц:")
    print(m1.add(m2))
    print("Вычитание матриц:")
    print(m1.subtract(m2))
    m3 = Matric(3, 2)
    m3.data = [[1, 2], [3, 4], [5, 6]]
    print("Умножение матриц:")
    print(m1.multiply(m3))
    print("Транспонирование матрицы 1:")
    print(m1.transpose())