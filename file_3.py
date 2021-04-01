# Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление
# до целого числа деления клеток соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
class Cages:
    def __init__(self, number_of_cells):
        if number_of_cells > 0 and type(number_of_cells) == int:
            self.number_of_cells = number_of_cells
        else:
            self.number_of_cells = 1

    def __add__(self, other):

        return f'Сумма всех клеток:{self.number_of_cells + other.number_of_cells}'

    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return f'Количество клеток при вычитании: {self.number_of_cells - other.number_of_cells}'
        else:
            return f'Количество клеток при вычитании:{other.number_of_cells - self.number_of_cells}'

    def __truediv__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return f'Количество клеток при делении:{(self.number_of_cells / other.number_of_cells): .0f}'
        else:
            return f'Количество клеток при делении:{(other.number_of_cells / self.number_of_cells): .0f}'

    def __mul__(self, other):
        return f'Количество клеток при умножении:{self.number_of_cells * other.number_of_cells}'


A = Cages(48)
B = Cages(10)
print(A+B)
print(A-B)
print(A*B)
print(A / B)
