
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


H1 = House('ЖК лето', 6)
H2 = House('ЖК Кремлевский',10)
H1.go_to(10)
H2.go_to(6)
