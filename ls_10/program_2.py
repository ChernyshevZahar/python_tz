import random

class man:
    def __init__(self,name,house):
        self.name = name
        self.hungry = 50
        self.house = house
    
    def eating(self):
        self.hungry += 1
        self.house.eat -= 1 


    def work(self):
        self.hungry -= 1 
        self.house.add_money(1)

    def play(self):
        self.hungry -= 1
    
    def buyEat(self):
        if self.house.money > 0:
            self.house.byeEat(1,1)
        else:
            print('нет денег мой лорд')

    def survival(self):
        if self.hungry <= 0:
            print('вы мертвы!')
            return
        num = random.randint(1,6)

        if self.hungry < 20:
            self.eating()
        elif self.house.eat < 10:
            self.buyEat()
        elif self.house.money < 50:
            self.work()
        elif num == 1:
            self.work()
        elif num == 2:
            self.eating()
        else:
            self.play()
        
    
    def info_man(self):
        print(f'сытость {self.name} = {self.hungry}, еда петра = {self.house.eat}, деньги петра = {self.house.money}')


class home:

    def __init__(self):
        self.eat = 50
        self.money = 0

    def byeEat(self,eat,money):
        self.eat += eat
        self.money -= money
        print(F'вы купили {eat} еды' )
    def add_money(self,money):
        self.money += money
        print(F'вы заработали {money} денег' )
    

if __name__ == '__main__':
    house1 = home()
    petr = man('Petr',house1)
    for day in range(1,366):
        petr.survival()
        petr.info_man()
        print(f'прошло {day} дней')
