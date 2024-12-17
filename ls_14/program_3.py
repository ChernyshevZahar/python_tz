import doctest

class Rectangle:
    def __init__(self,width = 0, height = 0 ):
        """
        >>> r = Rectangle(2,3)
        >>> r.get_aray()
        6
        >>> r.get_perimetr()
        10
        """



        self.width = width
        self.height = height
    
    def set_dimensions(self, width, height):
        """
        >>> r = Rectangle()
        >>> r.set_dimensions(6, 7)
        >>> r.get_aray()
        42
        >>> r.get_perimetr()
        26
        """
        if width <= 0 and height <= 0:
           raise ValueError('высота или шерина не может быть ровна 0')
        self.width = width
        self.height = height
    
    def get_aray(self):
        return self.width * self.height
    def get_perimetr(self):
        return 2*(self.width + self.height)
    

if __name__ == "__main__":
    doctest.testmod()