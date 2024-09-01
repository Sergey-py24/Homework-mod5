

class House:


    def __init__(self, name, num_of_floors: int):
        if not isinstance(num_of_floors, int):
            raise TypeError("ОШИБКА")
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to(self,my_floor):
        if my_floor < 1 or my_floor > self.num_of_floors:
            print('Нет такого этажа')
        for i in range(1, my_floor + 1):
            if i <= my_floor <= self.num_of_floors:
                print(i)




    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f'Название: {self.name},количество зтажей: {self.num_of_floors}'

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError ('Ошибка типа данных')
        self.num_of_floors += value
        return self

    def __iadd__(self, value):
        self.num_of_floors += value
        return self

    def __radd__(self, value):
        self.num_of_floors += value
        return self

    def __eq__(self, other):
        if not isinstance(other, House):
            raise TypeError('Ошибка')
        return self.num_of_floors == other.num_of_floors


    def __lt__(self, other):
        return self.num_of_floors < other.num_of_floors

    def __gt__(self, other):
        return self.num_of_floors > other.num_of_floors

    def __le__(self, other):
        return self.num_of_floors <= other.num_of_floors

    def __ge__(self, other):
        return self.num_of_floors >= other.num_of_floors

    def __ne__(self, other):
        return self.num_of_floors != other.num_of_floors





H1 = House('ЖК Лето', 10)
H2 = House('ЖК Кремлевский',20)
print(H1)
print(H2)
print(H1 == H2)    # eq
H1 = H1 + 10       # add
print(H1)
print(H1 == H2)
H1 += 10        # iadd
print(H1)
H2 = 10 + H2       # radd
print(H2)
print(H1 > H2)     # gt
print(H1 >= H2)    # ge
print(H1 < H2)     # lt
print(H1 <= H2)    # le
print(H1 != H2)    # ne

