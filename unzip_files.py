import os
import argparse
import zipfile
import fnmatch
from zipfile import ZipFile, is_zipfile

ROOT_PATH = '.'
PATTERN = '*.zip'

def unzip_files_in_folder(folder: str) -> list[str]:
    """
    Extract all zip files in the current directory recursively.
    
    Return a list of folders with the inziped dirs.
    """
    new_dirs = []
    for root, dirs, files in os.walk(folder):
        for filename in fnmatch.filter(files, PATTERN):
            dir = os.path.join(root, os.path.splitext(filename)[0])
            new_dirs.append(dir)
            zipfile.ZipFile(os.path.join(root, filename)).extractall(dir)
    return new_dirs


def extract_zip(input_zip: str) -> str:
    """
    Extract a zip file into the current directory.
    
    Returns the directory.
    """
    path, filename = os.path.split(input_zip)
    filename = os.path.splitext(filename)[0]
    dir = os.path.join(path, filename)
    ZipFile(input_zip).extractall(dir)
    return dir


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MPS-P5.")
    parser.add_argument('file', type=str, help="Zip file with the students' tasks.")
    args = parser.parse_args()

    dir = extract_zip(args.file)
    dir_list = unzip_files_in_folder(dir)
    print(dir_list)

    #unzip_files_in_folder(ROOT_PATH)
