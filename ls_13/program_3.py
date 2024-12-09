import random
import os

magic_num = 777


class MagicFileProcessor:

    def __init__(self,file):
        self.namefile = file
        self.path_file = self.get_path()
        self.num = 0
    def get_path(self):
        return os.path.join(os.path.abspath('.'), self.namefile)
    
    def remove_file(self):
        try:
            os.remove(self.path_file)
        except OSError as ex:
            print(ex)
            print('Данный файл не может быть удален')
    def esnum(self):
        return random.randint(1,13) == 5
    def add_num(self):
        

        try:

            num = int(input('Введите число: '))
            self.num += num
            if self.esnum():
                raise Exception('Вас постигла неудача!')
                
            
            with open(self.namefile, 'a', encoding="utf-8" ) as file:
                file.write(f'{num}\n')

        
        except Exception as e:
            print(e) 

    def run(self):

        self.remove_file()
        while self.num < magic_num:
                self.add_num()
        print('Вы успешно выполнили условие для выхода из порочного цикла!')


if __name__ == "__main__":
    mn = MagicFileProcessor('out_file.txt')
    mn.run()