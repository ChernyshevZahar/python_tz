num1= int(input('num1:'))
num2= int(input('num2:'))




while num2:
    num1, num2 = num2, num1 % num2 

print(num1)