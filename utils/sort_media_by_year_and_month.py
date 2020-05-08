#!/usr/bin/env python
import os
import re
from shutil import move
from PIL import Image
import sys
import subprocess
from enum import Enum

imageExtensions = [".JPG", ".jpg", ".jpeg", ".JPEG", ".png", ".PNG"]
videoExtensions = [".mp4", ".MP4", ".mov", ".MOV", ".m4v", ".M4V"]


class MediaType(Enum):
    IMAGE = 1
    VIDEO = 2


destination = "F:/ALL_MEDIA/Videos/"


def getCreationDate(fileName):
    if any(s in fileName for s in imageExtensions):
        image = Image.open(fileName)
        image.verify()
        return image._getexif()[36867]
    else:
        if any(s in fileName for s in videoExtensions):
            result = subprocess.Popen(['hachoir-metadata', fileName, '--raw', '--level=6'],
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            results = result.stdout.read().decode('utf-8').split('\n')
            creation_date = ''
            for item in results:
                if item.startswith('- creation_date: '):
                    creation_date = item.lstrip('- creation_date: ')
            return creation_date
    return ""


def createDateFoldersAndMoveMedia(dateString, fileName, fullFileName):
    year = re.findall('(\d{4}):\d{2}:\d{2}', dateString)
    if(len(year) == 0):
        year = re.findall('(\d{4})-\d{2}-\d{2}', dateString)
    month = re.findall('\d{4}:(\d{2}):\d{2}', dateString)
    if(len(month) == 0):
        month = re.findall('\d{4}-(\d{2})-\d{2}', dateString)
    newDir = destination + year[0] + "/" + month[0]
    os.makedirs(newDir, exist_ok=True)
    move(fullFileName, os.path.join(newDir, fileName))
    return True


def organizeMediaByDateFolders(srcdir, mediaType):
    srcFiles = os.listdir(srcdir)
    counter = 0
    errorCount = 0
    fileExtensions = imageExtensions
    if(mediaType == MediaType.VIDEO):
        fileExtensions = videoExtensions
    for fileName in srcFiles:
        fullFileName = os.path.join(srcdir, fileName)
        if (not os.path.isdir(fullFileName)):
            if any(s in fileName for s in fileExtensions) and not fileName.startswith('.'):
                try:
                    counter = counter + 1
                    creationDate = getCreationDate(fullFileName)
                    moveResult = createDateFoldersAndMoveMedia(
                        creationDate, fileName, fullFileName)
                except Exception as e:
                    errorCount = errorCount + 1
                    #print("Error copying file " + fileName + " with error " + e)
                    print("Error copying " + fileName)
        if (counter == 3000):
            break
    print("Total number of errors: " + str(errorCount))


organizeMediaByDateFolders("F:/ALL_MEDIA/Videos", MediaType.VIDEO)
