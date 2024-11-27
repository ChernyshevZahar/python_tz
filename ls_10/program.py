class child:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.cocst = 'cray'
        self.hunger = True


    def cahdgecocst(self, charge):
        self.cocst =  charge

    def cahdgehunger(self):
        self.hunger = False


class parent:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.children = []

    def getCildrenEat(self,children):
        children.cahdgehunger()

    def getCildrenCocst(self,children,charge):
        children.cahdgecocst(charge)

    def addcildren(self,cildren):
        if cildren.age > self.age - 16:
            print('незя!')
        else:
            self.children.append(cildren) 

    def cilde_info(self):
        for cilde in self.children:
            print(f'Ваш ребенок: {cilde.name}, голод : {cilde.hunger} настрой: {cilde.cocst}')


Parent = parent('bob', 27)
reb1 = child('cil' , 17)


if __name__ == '__main__':

    Parent.addcildren(reb1)


    Parent.cilde_info()

    Parent.getCildrenEat(reb1)

    Parent.cilde_info()

    Parent.getCildrenCocst(reb1,'fappy')

    Parent.cilde_info()