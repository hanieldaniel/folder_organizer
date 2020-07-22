import os
import shutil
import glob

# get current directory and list the files and folders
current_dir = os.getcwd()
list_of_files_and_folders = os.listdir(current_dir)

# Set of folders to be excluded
folders_list = {
    'Folders',
    'Image files',
    'Excel Files',
    'Docs and ppts',
    'PDF files',
    'Executables',
    'Archives',
    'Other files'
}

# create basic folders from folder list

for folder in folders_list:
    if not os.path.exists(os.path.join(current_dir, folder)):
        os.makedirs(os.path.join(current_dir, folder))

# Move all file from one diectory to another


def moveAllFilesinDir(srcDir, dstDir):
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)

    # Check if both the are directories
    if os.path.isdir(srcDir) and os.path.isdir(dstDir):
        # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '\/*'):
            # Move each file to destination Directory
            shutil.move(filePath, dstDir)
        shutil.rmtree(srcDir)
    else:
        print("srcDir & dstDir should be Directories")


for file in list_of_files_and_folders:

    filename, extension = os.path.splitext(file)

    current_folder = os.path.join(current_dir, file)
    dest_folder = os.path.join(current_dir, 'Folders', file)

    if file != 'folder_organizer.exe':
        if not extension:
            # Check if it is an organiser folder
            if filename not in folders_list:
                moveAllFilesinDir(current_folder, dest_folder)

        else:
            if extension in ('.jpg', '.png', '.gif'):
                shutil.move(
                    os.path.join(current_dir, file),
                    os.path.join(current_dir, 'Image files', file))
            elif extension in ('.xls', '.xlsx', '.xltx', '.xlsm'):
                shutil.move(
                    os.path.join(current_dir, file),
                    os.path.join(current_dir, 'Excel files', file))
            elif extension in ('.doc', '.docx', '.ppt', '.pptx'):
                shutil.move(
                    os.path.join(current_dir, file),
                    os.path.join(current_dir, 'Docs and ppts', file))
            elif extension in ('.pdf'):
                shutil.move(
                    os.path.join(current_dir, file),
                    os.path.join(current_dir, 'PDF files', file))
            elif extension in ('.bat', '.exe'):
                shutil.move(
                    os.path.join(current_dir, file),
                    os.path.join(current_dir, 'Executables', file))
            elif extension in ('.zip', '.rar', '.tar', '.iso', '.tar.gz', '.7z'):
                shutil.move(
                    os.path.join(current_dir, file),
                    os.path.join(current_dir, 'Archives', file))
            else:
                shutil.move(
                    os.path.join(current_dir, file),
                    os.path.join(current_dir, 'Other files', file))