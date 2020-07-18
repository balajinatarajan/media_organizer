import os


def deleteEmptyDirsRecursively(dirName):
    listOfEmptyDirs = list()

    listOfEmptyDirs = [dirpath for (dirpath, dirnames, filenames) in os.walk(
        dirName) if len(dirnames) == 0 and len(filenames) == 0]

    if len(listOfEmptyDirs) != 0:
        for elem in listOfEmptyDirs:
            print("Deleting folder " + elem)
            os.rmdir(elem)
        deleteEmptyDirsRecursively(dirName)
    return


if __name__ == '__main__':
    deleteEmptyDirsRecursively('F:/NewOrganized/Pictures')
