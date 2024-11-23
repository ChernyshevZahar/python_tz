import json
from functools import wraps
import csv

from typing import Callable 


def counter(fucn:callable):
    
    @wraps(fucn)
    def wrapper(*agrc:any, **kwargs:any):

        wrapper.count += 1
        result = fucn(*agrc,**kwargs)

        print(f'функцию использовали {wrapper.count} раз')
        return result
    wrapper.count = 0
    return wrapper    



@counter
def create_csv(directory,name_csv):

    data_file = []

    with open(directory, "r") as file_json:
        data_file.extend(json.load(file_json))

    with open(name_csv,"w",newline="") as file_csv:
        writecsv = csv.DictWriter(file_csv, fieldnames=["name","price","quantity"])
        writecsv.writeheader()
        writecsv.writerows(data_file)



if __name__ == '__main__':
    for _ in range(1,5,1):
        create_csv('test.json','test.cvs')