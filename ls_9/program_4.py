from typing import Callable


def cashe(func: callable):
    cashe = {} 
    def wrapper(number):
        
        if number in cashe:
            return cashe[number]
        else:
            result = func(number)
            cashe[number] = result
            return result

  
    return wrapper     


@cashe
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == '__main__':
    print(fibonacci(100))
    print(fibonacci(100))
