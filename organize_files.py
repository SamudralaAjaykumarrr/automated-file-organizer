import os
import shutil

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Others': []
}

folder_path = os.getcwd()

for folder in file_types:
    folder_dir = os.path.join(folder_path, folder)
    if not os.path.exists(folder_dir):
        os.mkdir(folder_dir)

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file_name)[1].lower()
        moved = False
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, file_name))
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(folder_path, 'Others', file_name))

print("✅ Files organized successfully!")
