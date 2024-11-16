import os 


def find_extension(directory, extension):

    for root,dic, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root,file))



find_extension('../ls_7','.txt')