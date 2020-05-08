import os
import shutil

imageExtensions = [".JPG", ".jpg", ".jpeg", ".JPEG", ".png", ".PNG"]
videoExtensions = [".mp4", ".MP4", ".mov", ".MOV", ".m4v", ".M4V"]


def countFilesRecursively(srcdir, count):
    srcFiles = os.listdir(srcdir)
    for fileName in srcFiles:
        fullFileName = os.path.join(srcdir, fileName)
        if (os.path.isdir(fullFileName)):
            count = countFilesRecursively(
                fullFileName, count)
        else:
            if not fileName.startswith('.') and (any(s in fileName for s in imageExtensions) or any(s in fileName for s in videoExtensions)):
                count = count + 1
    return count


src = "F:/California and unsorted pictures"
count = countFilesRecursively(src, 0)
print("Total media: " + str(count))
