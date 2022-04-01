import os
import argparse
import re

def delDirVirus(fol):
    for root, dirs, files in os.walk(fol):
        filename = str(root).split('/')[-1]
        pattern = fr'^({filename})+(\s|)+(.exe)$'
        for file in filter(lambda x: re.match(pattern,x), files):
            os.remove(os.path.join(root,file))

def delUnhideVirus(fol):
    for root, dirs, files in os.walk(fol):
        filename = str(root).split('/')[-1]
        filename = re.escape(filename)
        pattern = fr'^({filename})+(\s|)+(.exe)$'
        unhide_pattern = r'\b(unhide files\.bat)\b'
        for file in filter(lambda x: re.match(pattern,x), files):
            os.remove(os.path.join(root,file))
        for file in filter(lambda x: re.match(unhide_pattern, x,re.IGNORECASE),files):
            os.remove(os.path.join(root,file))

def main():
    #parsing the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("fol",nargs='?', help="Directory to enter", default=None)
    args = parser.parse_args()
    if(args.fol):
        #passing the command line argument with the folder path to delete directory named virus and unhide files.bat file
        delUnhideVirus(args.fol)
        #passing the command line argument with the folder path to delete diretory named virus
        # delDirVirus(args.fol)
    else:
        for dir in filter(os.path.isdir, os.listdir(os.getcwd())):
            delUnhideVirus(dir)
            
if __name__ == '__main__':
    main()
