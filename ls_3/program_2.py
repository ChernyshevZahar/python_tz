
numbers = [int(x) for x in input("Введите числа через пробел:").split()]

max_number = numbers[0]

for num in numbers:


    if num > max_number:
        max_number = num
print(max_number)