import os
import shutil

source_folder = input("Enter folder path: ")
print(os.listdir(source_folder))

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):

        ext = file.split(".")[-1].lower()

        folder_name = ext.upper() + "_Files"
        destination_folder = os.path.join(source_folder, folder_name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        shutil.move(file_path,
                    os.path.join(destination_folder, file))

print("Files Organized Successfully!")