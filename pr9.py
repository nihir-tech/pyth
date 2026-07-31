import os
import zipfile
folder_name = input("Enter folder name: ")
zip_name = folder_name + ".zip"
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
    for folder, subfolders, files in os.walk(folder_name):
        for file in files:
            file_path = os.path.join(folder, file)
            zipf.write(file_path)
print("Backup completed successfully.")
print("ZIP file created:", zip_name)
