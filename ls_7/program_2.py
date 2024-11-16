import os

import zipfile


def zip_directory(source_dir, output_zip):

   with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipw:
      
      for root,dir, files in os.walk(source_dir):
         for file in files:
            path_file = os.path.join(root, file)
            zipw.write(path_file, os.path.relpath(path_file,source_dir))


                
zip_directory('files','files.zip')