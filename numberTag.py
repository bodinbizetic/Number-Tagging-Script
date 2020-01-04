from os import listdir
import os
from math import log10, ceil
from os.path import isfile, join

def getAllFilesWithExtension(extension='.jpg'):
    mypath = os.getcwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and os.path.splitext(join(mypath, f))[1] == extension]
    return onlyfiles

def sortCompareFunction(key):
    return os.path.getctime(join(os.getcwd(), key))

def sortByDateModified(filesListToBeTagged):
    filesListToBeTagged.sort(key=sortCompareFunction)
    pass

def taggItemsNumbers(filesListToBeTagged, prefix=""):
    for i, file in enumerate(filesListToBeTagged):
        os.rename(join(os.getcwd(), file), join(os.getcwd(), prefix + "0"*(ceil(log10(len(filesListToBeTagged)))-ceil(log10(i+2)))+str(i) + ".jpg")) #change for more than 100 files


def main():
    filesListToBeTagged = getAllFilesWithExtension()
    sortByDateModified(filesListToBeTagged)
    taggItemsNumbers(filesListToBeTagged, "DisK3_")
    pass

if __name__ == "__main__":
    main()