
n = int(input('Введите количество чисел в последовательности: '))


count = 0

for i in range(n):

    number = int(input('Введите очередное число: '))
   
    if number > 1: 
        for divider in range(2, number):
        
            if number % divider == 0:
                break
            else:
            
                count += 1
            
            print('Количество простых чисел:', count)
