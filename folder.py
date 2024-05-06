import os
import shutil



downloads_folder_path = r'C:\Users\joaol\Downloads'

for file in os.listdir(downloads_folder_path):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
    
    folder_to_organization_file = f'{downloads_folder_path}/{file_extension}'

    if not os.path.isdir(folder_to_organization_file):
        os.mkdir(folder_to_organization_file)

    shutil.move(f'{downloads_folder_path}/{file}', f'{folder_to_organization_file}/{file}')