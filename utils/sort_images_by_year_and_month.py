#!/usr/bin/env python
import os
import re
from shutil import move
from PIL import Image
import sys

imageExtensions = [".JPG", ".jpg", ".jpeg", ".JPEG", ".png", ".PNG"]
videoExtensions = [".mp4", ".MP4", ".mov", ".MOV", ".m4v", ".M4V"]
mediaRoot = "/Users/bala/tmp/"


def getCreationDate(fileName):
    image = Image.open(fileName)
    image.verify()
    return image._getexif()[36867]


def createDateFoldersAndMoveMedia(dateString, fileName, fullFileName):
    try:
        year = re.findall('(\d{4}):\d{2}:\d{2}', dateString)
        month = re.findall('\d{4}:(\d{2}):\d{2}', dateString)
        newDir = mediaRoot + year[0] + "/" + month[0]
        os.makedirs(newDir, exist_ok=True)
        move(fullFileName, os.path.join(newDir, fileName))
        return True
    except:
        print("Error moving " + fullFileName + ".." + sys.exc_info()[0])
        return False


def organizeImagesByDateFolders(srcdir):
    srcFiles = os.listdir(srcdir)
    for fileName in srcFiles:
        fullFileName = os.path.join(srcdir, fileName)
        if (not os.path.isdir(fullFileName)):
            if any(s in fileName for s in imageExtensions):
                imageCreationDate = getCreationDate(fullFileName)
                moveResult = createDateFoldersAndMoveMedia(
                    imageCreationDate, fileName, fullFileName)
                if (not moveResult):
                    print(fileName)


organizeImagesByDateFolders(
    "/Users/bala/tech/workspace/python/filesorter/test")
