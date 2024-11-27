class Animal:

    def __init__(self, name):
        self.name = name

class Bird(Animal) :
    def __init__(self, name,wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    def wing_length(self):
        return self.wingspan/2
class Fish(Animal):
    def __init__(self, name,max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'мелководная'
        elif self.max_depth > 100:
            return 'глубоководная'
        else:
            return 'средневодная'

class Mammal(Animal):
    def __init__(self, name,weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        else:
            return 'Обычный'
        
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, *args) -> Animal:
        """
        Создает экземпляр животного на основе переданного типа и
        параметров.
        :param animal_type: Название типа животного (например, 'Dog'
        или 'Cat')
        :param args: Параметры для конструктора животного
        :return: Экземпляр соответствующего класса животного
        """
        animal_classes = {
        'Bird': Bird,
        'Fish': Fish,
        'Mammal':Mammal
        }
        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
        

if __name__ == "__main__":
    Bird_1 = AnimalFactory.create_animal('Bird', 'ptichka', 12) 
    print(Bird_1.wing_length())