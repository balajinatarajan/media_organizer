import os
from enum import Enum
import MySQLdb
from shutil import move


imageExtensions = [".JPG", ".jpg", ".jpeg", ".JPEG", ".png", ".PNG"]
videoExtensions = [".mp4", ".MP4", ".mov", ".MOV", ".m4v", ".M4V"]


class MediaType(Enum):
    IMAGE = 1
    VIDEO = 2


destination = "F:/NewOrganized/dupes-discard"
totalFilesToBeProcessed = 4

# mydb = MySQLdb.Connect(host="192.168.1.28", port=3306, user="root", passwd="Team123!", db="mediaorganizer"
#                        )

mydb = MySQLdb.Connect(host="localhost", user="root", passwd="Team123!", db="mediaorganizer"
                       )


def getDuplicateFilesList():
    mycursor = mydb.cursor()
    mycursor.execute(
        """select
  fullfilename
from mediaindex
where
  source = "Stage"
  and filetype = "Image"
  and filehash in (
    select
      filehash
    from mediaindex
    where
      source = "Live"
      and filetype="Image"
  )""")
    files = mycursor.fetchall()
    return files


def markvoid(file):
    mycursor = mydb.cursor()
    mycursor.execute(
        "UPDATE mediaindex SET void = 'yes' WHERE fullfilename = %s", (file,))
    mydb.commit()


def moveFiles(files):
    filesCount = 0
    errorCount = 0
    for file in files:
        try:
            filesCount += 1
            # print(file[0])
            move(file[0], destination)
            markvoid(file[0])
            if(filesCount > totalFilesToBeProcessed):
                break
        except:
            errorCount += 1
    print("Total number of errors: " + str(errorCount))


moveFiles(getDuplicateFilesList())
