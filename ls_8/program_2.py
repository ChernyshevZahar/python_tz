import glob

import json


def merge_json_files(input_files, output_file):
    
    data_json = []

    for list in input_files:
        print(list)
        with open(list,'r') as file_json:
            data_json.extend(json.load(file_json))

    with open(output_file, "w") as file_end_json:
        json.dump(data_json, file_end_json, indent=4)


if __name__ == "__main__":
    
    json_files = glob.glob('files/zad_2/employees*.json')
    
    merge_json_files(json_files, 'all_employees.json')