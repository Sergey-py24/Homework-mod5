
class House:
    constr_history = []

    def __new__(cls, *args, **kwargs):
        cls.constr_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, num_of_floors: int):
        if not isinstance(num_of_floors, int):
            raise TypeError("ОШИБКА")
        self.name = name
        self.num_of_floors = num_of_floors

    def __del__(self):
        print(f'{self.name} остался только в Википедии')


H1 = House('ЖК Лето', 10)
print(House.constr_history)
H2 = House('ЖК Кремлевский', 20)
print(House.constr_history)
H3 = House('ЖК Старый',30)
print(House.constr_history)
del H2
del H3
print(House.constr_history)

