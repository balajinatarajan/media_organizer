import MySQLdb
import os
import re
import imagehash
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


source = "Stage"
totalFilesToBeProcessed = 100000
errorCount = 0
filesCount = 0

mydb = MySQLdb.Connect("localhost", "root", "Team123!", "mediaorganizer"
                       )


def hashFile(file):
    hashes = []
    img = Image.open(file)
    # hash the image 4 times and rotate it by 90 degrees each time
    for angle in [0, 90, 180, 270]:
        if angle > 0:
            turned_img = img.rotate(angle, expand=True)
        else:
            turned_img = img
        hashes.append(str(imagehash.phash(turned_img)))
    hashes = ''.join(sorted(hashes))
    return hashes


def storeMetadata(fileName, fullFileName, mediaType):
    fileType = "Video" if mediaType == MediaType.VIDEO else "Image"
    yearMatch = re.findall(
        '/(\d{4})/', fullFileName) if os.sep == '/' else re.findall('\\\\(\d{4})\\\\', fullFileName)
    monthMatch = re.findall(
        '/(\d{2})/', fullFileName) if os.sep == '/' else re.findall('\\\\(\d{2})\\\\', fullFileName)
    fileSize = os.stat(fullFileName).st_size
    fileHash = hashFile(fullFileName) if mediaType == MediaType.IMAGE else "NA"
    mycursor = mydb.cursor()
    sql = "insert into mediaindex (source,filetype,year,month,filename,fullfilename,filesize,filehash) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (source, fileType, int(yearMatch[0]), int(
        monthMatch[0]), fileName, fullFileName, int(fileSize), fileHash)
    mycursor.execute(sql, val)
    mydb.commit()


def extractMetadata(srcdir, mediaType):
    srcFiles = os.listdir(srcdir)
    global filesCount
    global errorCount
    fileExtensions = imageExtensions
    if(mediaType == MediaType.VIDEO):
        fileExtensions = videoExtensions
    for fileName in srcFiles:
        fullFileName = os.path.join(srcdir, fileName)
        if(not fileName.startswith('.')):
            if (os.path.isdir(fullFileName)):
                extractMetadata(fullFileName, mediaType)
            else:
                if any(s in fileName for s in fileExtensions):
                    try:
                        filesCount = filesCount + 1
                        storeMetadata(fileName, fullFileName, mediaType)
                    except Exception as e:
                        errorCount = errorCount + 1
                        print("Error extracting metadata " + fileName + " with error " + e)
                        #print("Error extracting metadata " + fullFileName)
        if(filesCount%200 == 0):
            print("Total files processed: " + str(filesCount))
        if (filesCount == totalFilesToBeProcessed):
            break
    print("Total number of errors: " + str(errorCount))


extractMetadata("F:/NewOrganized/Pictures", MediaType.IMAGE)
