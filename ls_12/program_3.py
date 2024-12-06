class Book:
    _id_counter = 1 


    def __new__(cls, *args, **kwargs):
        instanse = super().__new__(cls)
        instanse.id = cls._id_counter
        cls._id_counter += 1
        return instanse
    
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor

    def __str__(self):
        return f'title {self.title}, autor {self.autor}, id {self.id}'
    

if __name__ == "__main__":
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    print(book1)
    print(book2)

