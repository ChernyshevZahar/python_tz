import random


max_carma = 500

class KillError(Exception):
    def __init__(self):
        super().__init__('Убийство. Вы и убили-с!')

class DrunkError(Exception):
    def __init__(self):
        super().__init__('Пьянство. Пьянству бой!')

class CarCrashError(Exception):
    def __init__(self):
        super().__init__('Вы попали в аварию. Стоит следить за дорогой.')

class GluttonyError(Exception):
    def __init__(self):
        super().__init__('Вы обожрались. Следует сократить порции.')

class DepressionError(Exception):
    def __init__(self):
        super().__init__('На вас напала хандра. Уныние - грех.')


def oneday():

    carma = random.randint(1,7)



    if random.randint(1,10) == 5:

        exseption = random.choice([KillError(),DrunkError(),CarCrashError(),GluttonyError(),DepressionError()])

        raise exseption
    
    return carma



def main():
    carma = 0
    day = 0
    with open('karma.log', 'w', encoding="utf-8" ) as file:
        while carma < max_carma:
            try: 
                carma += oneday()
                day += 1
            except Exception as e: 
                file.write(f'{e}\n')
        print(f'Ваша карма {carma} за {day} дней')  
        file.close() 



if __name__ == "__main__":

    main()

        



