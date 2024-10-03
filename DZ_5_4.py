class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(f'{i+1}')
    def __len__(self):
        return (self.number_of_floors)

    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        else:
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        else:
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floors <= other
        else:
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        else:
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floors >= other
        else:
         return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floors != other
        else:
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

        # if isinstance(other, int) and other == 0:
        #     return self
        # else:
        #     return self.__add__(other)


    def __iadd__(self, other):
        self.number_of_floors += other
        return House(self.name, self.number_of_floors)

    def __del__(self):
        print(f'{self.name} снесен, но он остался в истории')
        #return (f'{self.name} снесен, но он остался в истории')


h1 = House("ЖК Эльбрус",10)
print(House.houses_history)
h2 = House("ЖК Акация", 20)
print(House.houses_history)
h3 = House("ЖК Матрешка", 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)



