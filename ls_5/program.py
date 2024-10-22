def functin_generate(n:int):
    for i in range(1,n+1):
        yield i ** 2



def main():
    n = int(input('num:'))

    for num in functin_generate(n):
        print(num)

n = int(input('num:'))
generator_expr = (i ** 2 for i in range(1, n + 1))
for square in generator_expr:
    print(square, end=' ')
    print()

# main()