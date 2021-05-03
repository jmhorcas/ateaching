"""
    This script search for text content in each file inside a folder (recursively).
    It prints the paths of those files containing the piece of text provided.
"""

import os 
import argparse


def main(directory: str, text: str, extension: str):
    filelist = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("." + extension):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    if text in content:
                        filelist.append(os.path.join(root, file))

    for file in filelist:
        print(file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Identify suspicious copies between students' deliverables.")
    parser.add_argument('-f', '--folder', dest='folder', type=str, required=True, help="Folder to search for recursively.")
    parser.add_argument('-t', '--text', dest='text', type=str, required=True, help="Text to search for.")
    parser.add_argument('-ext', '--extension', dest='extension', type=str, required=True, help="Extension file to look into (e.g., 'java', 'py').")
    args = parser.parse_args()

    main(args.folder, text=args.text, extension=args.extension)