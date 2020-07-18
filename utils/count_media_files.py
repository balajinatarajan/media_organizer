import os
import shutil

imageExtensions = [".JPG", ".jpg", ".jpeg", ".JPEG", ".png", ".PNG"]
videoExtensions = [".mp4", ".MP4", ".mov", ".MOV", ".m4v", ".M4V"]

fileSizeLowerLimit = 0
errorCount = 0

def countFilesRecursively(srcdir, count):
    global errorCount
    srcFiles = os.listdir(srcdir)
    for fileName in srcFiles:
        fullFileName = os.path.join(srcdir, fileName)
        if (os.path.isdir(fullFileName)):
            count = countFilesRecursively(
                fullFileName, count)
        else:
            if not fileName.startswith('.') and (any(s in fileName for s in imageExtensions) or any(s in fileName for s in videoExtensions)):
                try:
                    fileSize = os.stat(fullFileName).st_size
                    if(fileSize > fileSizeLowerLimit):
                        count = count + 1
                        print(fullFileName)
                except:
                    errorCount = errorCount + 1
    return count


src = "G:/unsorted"
count = countFilesRecursively(src, 0)
print("Total media: " + str(count))
print("Total errors: " + str(errorCount))
