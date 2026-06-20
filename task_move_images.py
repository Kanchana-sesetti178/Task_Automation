import os
import shutil
source_folder = "Source_Folder"
destination_folder = "Destination_Folder"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

moved_count = 0

for file_name in os.listdir(source_folder):
    if file_name.endswith(".jpg"):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        shutil.move(source_path, destination_path)

        print("Moved:", file_name)
        moved_count += 1

print("\nTask Completed!")
print("Total JPG files moved:", moved_count)