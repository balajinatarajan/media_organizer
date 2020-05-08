import os
import shutil

otherFileTypes = []

imageExtensions = [".JPG", ".jpg", ".jpeg", ".JPEG", ".png", ".PNG"]
videoExtensions = [".mp4", ".MP4", ".mov", ".MOV", ".m4v", ".M4V"]

fileSizeLowerLimit = 200


def countFilesRecursively(srcdir, count):
    srcFiles = os.listdir(srcdir)
    for fileName in srcFiles:
        fullFileName = os.path.join(srcdir, fileName)
        if (os.path.isdir(fullFileName)):
            count = countFilesRecursively(
                fullFileName, count)
        else:
            if not fileName.startswith('.') and (any(s in fileName for s in imageExtensions) or any(s in fileName for s in videoExtensions)):
                fileSize = os.stat(fileName).st_size
                if(fileSize > fileSizeLowerLimit):
                    count = count + 1
                extn = ""
            try:
                extn = fileName.rsplit(".", 1)[1]
            except:
                pass
            if extn not in otherFileTypes:
                otherFileTypes.append(extn)
    return count


src = "/Volumes/MONTUX-2TB"
count = countFilesRecursively(src, 0)
print("Total media: " + str(count))
print(otherFileTypes)
