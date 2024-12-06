class Person:

    def __init__(self,name,age,email):
        self.__setattr__('name',name)
        self.__setattr__('age',age)
        self.__setattr__('email',email)

    def __setattr__(self, name, value):
        if name == "name":
            if not (value and value[0].isupper() and value.isalpha()):
                raise ValueError('Имя должно начитаться с большой буквы и состоять из букв')
                

        if name == "age":
            if not (isinstance(value,int) and 1 <= value <= 120):
                raise ValueError('Возраст может быть только в диапазоне от 1 до 120')
                
        if name == "email":

            if not ('@' in value):
                raise ValueError('Введите правильный емайл')
                

        super().__setattr__(name,value)

    def __str__(self):
        return f" имя {self.name }, возраст {self.age}, емайл {self.email} "

if __name__ == "__main__":
    try:
        ted = Person('Ted', 12, 'dsfd@gmail.ru')
        print(ted)
    except ValueError as e:
        print(e)