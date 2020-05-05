#!/usr/bin/env python
import os
import re
from shutil import move
from PIL import Image
import sys

imageExtensions = [".JPG", ".jpg", ".jpeg", ".JPEG", ".png", ".PNG"]
videoExtensions = [".mp4", ".MP4", ".mov", ".MOV", ".m4v", ".M4V"]
mediaRoot = "F:/ALL_MEDIA/Pictures/"


def getCreationDate(fileName):
	image = Image.open(fileName)
	image.verify()
	return image._getexif()[36867]


def createDateFoldersAndMoveMedia(dateString, fileName, fullFileName):
	year = re.findall('(\d{4}):\d{2}:\d{2}', dateString)
	month = re.findall('\d{4}:(\d{2}):\d{2}', dateString)
	newDir = mediaRoot + year[0] + "/" + month[0]
	os.makedirs(newDir, exist_ok=True)
	move(fullFileName, os.path.join(newDir, fileName))
	return True


def organizeImagesByDateFolders(srcdir):
	srcFiles = os.listdir(srcdir)
	counter = 0
	errorCount = 0
	for fileName in srcFiles:     
		fullFileName = os.path.join(srcdir, fileName)
		if (not os.path.isdir(fullFileName)):
			if any(s in fileName for s in imageExtensions) and not fileName.startswith('.'):
				try:
					counter = counter + 1
					imageCreationDate = getCreationDate(fullFileName)
					moveResult = createDateFoldersAndMoveMedia(imageCreationDate, fileName, fullFileName)
				except Exception as e:
					errorCount = errorCount + 1
					#print("Error copying file " + fileName + " with error " + e)
		if (counter == 20000):
			break
	print("Total number of errors: " + str(errorCount))


organizeImagesByDateFolders(
	"F:/ALL_MEDIA")
