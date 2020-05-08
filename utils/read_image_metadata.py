import os
from PIL import Image


def getImageMetadata(fileName):
    image = Image.open(fileName)
    image.verify()
    return image._getexif()


def getImageStat(fileName):
    return os.stat(fileName)


print(getImageStat('img.JPG').st_size)
