
class House:

    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to(self,my_floor):
        for i in range(1, my_floor + 1):
            if i <= my_floor <= self.num_of_floors:
                print(i)
            else:
                print('Нет такого этажа')
                break

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f'Название: {self.name},количество зтажей: {self.num_of_floors}'


H1 = House('ЖК лето', 9)
H2 = House('ЖК Кремлевский',10)
H1.go_to(int(input('Введите нужный этаж: ')))
H2.go_to(int(input('Введите нужный этаж: ')))
print(H1)
print(H2)
print(len(H1))
print(len(H2))