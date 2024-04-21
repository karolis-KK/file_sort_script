import os
import shutil

target_folder = "C:\Users\User\Documents\bandymas"
extensions = {item.split(".")[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}

# create folders
for extension in extensions:
    folder_path = os.path.join(target_folder, extension)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# move files
for item in os.listdir(target_folder):
    if os.path.isfile(os.path.join(target_folder, item)):
        file_extension = item.split(".")[-1]
        source_path = os.path.join(target_folder, item)
        destination_path = os.path.join(target_folder, file_extension, item)
        shutil.move(source_path, destination_path)
