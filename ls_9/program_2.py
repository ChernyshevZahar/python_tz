import time
from typing import Callable;

def slolytime (func :callable):

    def wraper(*agrc:any,**kwargs:any):
        time.sleep(2)
        result = func(*agrc,**kwargs)
        return result

    return wraper


@slolytime
def test():
    print(time.time())



if __name__ == '__main__':
    
    for i in range(1,4,1):
        test()