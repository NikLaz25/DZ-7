'''3.Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать
класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки
 (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов:
 сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
 Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
 и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
 исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества
ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
 количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество
ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n****x*..., где количество ячеек между \n равно
переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда м
етод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.'''
class Cell:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        self.x += other
        print('итог суммы', self.x)
    def __sub__(self, other):
        if self.x != other:
            self.x -= other
            print('итог разности', self.x)
        else:
            print('Значения равны, разница равна нулю')
    def __mul__(self, other):
        self.x *= other
        print('итог произведения', self.x)

    def __truediv__(self, other):
        self.x //= other
        print('итог частного', self.x)

    def make_order(self, y):
        print('задано кол-во ячеек в строке: ',y)
        z = self.x // y
        z1 = self.x % y
        while z:
            print('*' * y, '\n', end='')
            z -= 1
        print('*' * z1, '\n', end='')

new_ekz2 = Cell(24)
new_ekz2 + 12
new_ekz2 - 9
new_ekz2 * 2
new_ekz2 / 2
new_ekz2.make_order(5)

