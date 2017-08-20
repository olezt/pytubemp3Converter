import moviepy.editor as mp
from pytube import YouTube
import sys, os, shutil, string, random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def deleteTempFolder(tempFolderName):
    try:
        shutil.rmtree(tempFolderName)
    except:
        pass
            
def createNewTempFolder(tempFolderName):
    deleteTempFolder(tempFolderName)
    os.mkdir(tempFolderName)

def downloadVideo(url, tempFolderName):
    yt = YouTube(url)
    filename = yt.filename
    yt.set_filename('tempVideo')
    yt.videos[0].download(tempFolderName)
    return {'filename' : filename, 'extension' : yt.videos[0].extension}

def videoToMp3(tempFolderName, extension, filename):
    id = id_generator()
    clip = mp.VideoFileClip(tempFolderName + "tempVideo." + extension)
    clip.audio.write_audiofile("exported/" + filename + " " + id  + ".mp3")

def main():
    tempFolderName = 'temp/'
    if sys.argv[1]:
        deleteTempFolder(tempFolderName)
        createNewTempFolder(tempFolderName)
        videoResult = downloadVideo(sys.argv[1], tempFolderName)
        videoToMp3(tempFolderName, videoResult['extension'], videoResult['filename'])
        deleteTempFolder(tempFolderName)
    else:
        print ("Please enter a youtube url as argument")

main()
