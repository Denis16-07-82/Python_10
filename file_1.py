#  Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
#  который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
class Matrix:
    def __init__(self, *args):
        for ln in args[0]:
            string = str(ln).strip('[]')
            print(f'|{string}|')


p = [[3, 5, 8, 3], [8, 3, 7, 1], [1, 2, 3, 4]]
A = Matrix(p)


class Matrix_1:
    def __init__(self, *args):
        self.matrix = args

    def __str__(self):
        string=''
        for ln in self.matrix[0]:
            string+= '|'+str(ln).strip('[]')+'|'+'\n'
        return f'{string}'
B=Matrix_1(p)
print(B)
