import os


def batch_rename_files(directory, final_name, num_digits,old_extension, new_extension, name_range):

    
    
    if not os.path.isdir(directory):
        print(f'дириктории  {directory} нет')
        return
    
    if os.listdir(directory):
        files = [f for f in os.listdir(directory) if f.endswith(old_extension)]
    
        if not files:
            print(f"в директории {directory} нет файлов с разширением {old_extension}")
            return

    format_num = f"{{:0{num_digits}d}}"

    for index, file in enumerate(files,start=1):

        name_file = os.path.splitext(file)[0]

        if name_range:
            start, end = name_range
            split_name = name_file[start-1:end]

        else:
            split_name = name_file

        new_name_file = f"{split_name}{final_name}{format_num.format(index)}{new_extension}"

        new_path = os.path.join(directory,new_name_file)
        old_path = os.path.join(directory,file)

        os.rename(old_path,new_path)

        print(f"имя файла {old_path} заменено на {new_path}")

if __name__ == "__main__":

    import sys

    if len(sys.argv) != 6:
        print("Usage: python file_rename.py <directory> <final_name> <num_digits> <old_extension> <new_extension>")
        sys.exit()

    directory = sys.argv[1]
    final_name = sys.argv[2]
    num_digits = sys.argv[3]
    old_extension = sys.argv[4]
    new_extension = sys.argv[5]

    name_range = [3,6]


    batch_rename_files(directory,final_name,num_digits,old_extension,new_extension,name_range)