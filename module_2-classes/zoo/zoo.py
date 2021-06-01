class Animal():
    def __init__(self, color, legs) -> None:
        self.species = self.__class__.__name__
        self.color = color
        self.legs = legs

    def __repr__(self) -> str:
        return f'{self.color} {self.species}, {self.legs} legs'

class Wolf(Animal):
    def __init__(self, color) -> None:
        super().__init__(color, 4)

class Sheep(Animal):
    def __init__(self, color) -> None:
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color) -> None:
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color) -> None:
        super().__init__(color, 2)

class Cage():
    def __init__(self, id) -> None:
        self.animals = []
        self.id = id

    def add_animals(self, *args):
        for animal in args:
            self.animals.append(animal)

    def __repr__(self) -> str:
        animal_str = ''
        for a in self.animals:
            animal_str = animal_str + a.__repr__() + ' | '
        return f'Cage {self.id} contains: {animal_str}'

class Zoo():
    def __init__(self) -> None:
        self.cages = []

    def add_cages(self, *args):
        for cage in args:
            self.cages.append(cage)

    def __repr__(self) -> str:
        zoo_str = 'Zoo cages: '
        for cage in self.cages:
            zoo_str = zoo_str + cage.__repr__()
        
        return zoo_str

if __name__ == "__main__":
    wolf = Wolf('black')
    sheep = Sheep('white')
    snake = Snake('brown')
    parrot = Parrot('green')

    c1 = Cage(1)
    c1.add_animals(wolf, sheep)
    
    c2 = Cage(2)
    c2.add_animals(snake, parrot)
    
    z = Zoo()
    z.add_cages(c1, c2)
    
    print(z)