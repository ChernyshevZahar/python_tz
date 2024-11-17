import json

import csv



def create_csv(directory,name_csv):

    data_file = []

    with open(directory, "r") as file_json:
        data_file.extend(json.load(file_json))

    with open(name_csv,"w",newline="") as file_csv:
        writecsv = csv.DictWriter(file_csv, fieldnames=["name","price","quantity"])
        writecsv.writeheader()
        writecsv.writerows(data_file)

if __name__ == "__main__":

    create_csv('files/zad_3/products.json', "products.cvs")