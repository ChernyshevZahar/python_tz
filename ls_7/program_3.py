import os 

import time


def dell_file_on_time(directory,days):

    for root, dic, files in os.walk(directory):

         for file in files:
            path_file = os.path.join(root,file)
            if (time.time() - os.path.getatime(path_file))/86400 > days:
                os.remove(path_file)



dell_file_on_time('../ls_7', 1)