# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
class Clothes:
    def __init__(self, name, Size):
        self.name = name
        self.Size = Size

    @property
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return f'Общий расход материала на {self.name} и на {other.name}:{self.fabric_consumption + other.fabric_consumption} погонных метра'

    def __str__(self):
        return f'Расход материала на {self.name}:{self.fabric_consumption} погонных метра'


class Suit(Clothes):
    @property
    def fabric_consumption(self):
        return (2 * self.Size + 0.3)


class Coat(Clothes):
    @property
    def fabric_consumption(self):
        return (self.Size / 6.5 + 0.5)


A = Suit('Suit', 10)
B = Suit('Suit', 12)
C = Coat('Coat', 12)
D = Coat('Coat', 17)

print(A)
print(D)
print((A + D))
#Общую сумму не получается сделать-только для пары объектов.