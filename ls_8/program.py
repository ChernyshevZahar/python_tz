import os

import json

import csv

import pickle


def cheak_size(directory):

    if os.path.isfile(directory):
        return os.path.getsize(directory)
    elif os.path.isdir(directory):
        dir_size = 0
        for root,_,files in os.walk(directory):
            for file in files:
                path_file = os.path.join(root,file)
                dir_size += os.path.getsize(path_file)        
        return dir_size
    
def traverse_directory(directory):

    result = []

    for root , dir , files in os.walk(directory):

        for file in dir + files:
            file_path = os.path.join(root,file)
            is_dir = os.path.isdir(file_path)
            file_size = cheak_size(file_path)
            parent_path = os.path.basename(file_path)

            result.append(
                {
                    "name":file,
                    "path":file_path,
                    "type": "directory" if is_dir else "File",
                    "size":file_size,
                    "parent":parent_path
                }
        )
    return result


def save_to_json(data, name):
    with open(name, "w",) as file_json:
        json.dump(data,file_json,indent=4)
    
def save_to_csv(data, name):
    with open(name, "w", newline="") as file_cvs:
        writecvs = csv.DictWriter(file_cvs, fieldnames=["name","path","type","size","parent"])
        writecvs.writeheader()
        writecvs.writerows(data)

def save_to_pickle(data, name):
    with open(name, "wb") as file_pickle:
        pickle.dump(data,file_pickle)


def main(directory):
    
    data_path = traverse_directory(directory)

    save_to_json(data_path,"dicertory_path.json")
    save_to_csv(data_path,"dicertory_path.cvs")
    save_to_pickle(data_path,"dicertory_path.pickle")

if __name__ == "__main__":
    
    main('files')