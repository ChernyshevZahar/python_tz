from typing import Callable;

def how_are_you(fucn:callable):
    def wraper(*args: any, **kwargs: any):
        input("как дела?")
        print("А у меня не очень! Ладно, держи свою функцию")
        result = fucn(*args, **kwargs)
        return result
    return wraper

@how_are_you
def test(a=1):
    print(f'выпонена нужная {a} функция')


if __name__ == '__main__':

    test()