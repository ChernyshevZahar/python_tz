class Rectangle:
    def __init__(self,width,height=None):
        self.width = width
        self.height = height if height is not None else width
    def area(self):
            return self.height * self.width
    def perimeter(self):
        if self.height:
            return self.width * 4 
        else:
            return 2 * (self.height + self.width )
    
    def __add__(self, other):
        
        new_perimeter = self.perimeter() + other.perimeter()

        new_height = new_width = new_perimeter // 4 

        return Rectangle(new_width,new_height)
    def __sub__(self, other):
        
        new_perimeter = self.perimeter() - other.perimeter()

        new_height = new_width = new_perimeter // 4 

        return Rectangle(new_width,new_height)

    def __lt__(self, other):
        return self.area() < other.area()
    def __eq__(self, other):
        return self.area() == other.area()
    def __le__(self, other):
        return self.area() <= other.area()
    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    

if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)
    # Вывод периметра и площади
    print(f"Периметр rect1: {rect1.perimeter()}") # Вывод: 30
    print(f"Площадь rect2: {rect2.area()}") # Вывод: 21
    # Сравнение прямоугольников по площади
    print(f"rect1 < rect2: {rect1 < rect2}") # Вывод: False
    print(f"rect1 == rect2: {rect1 == rect2}") # Вывод: False
    print(f"rect1 <= rect2: {rect1 <= rect2}") # Вывод: False
    # Сложение и вычитание прямоугольников
    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}") # Вывод: 50
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}") # Вывод: 2
    # Дополнительный тест для repr и str
    print(rect3) # Вывод: Прямоугольник со сторонами 12 и 12
    print(repr(rect4)) # Вывод: Rectangle(2, 2)