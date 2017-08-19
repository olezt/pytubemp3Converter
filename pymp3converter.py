import moviepy.editor as mp
from pytube import YouTube
import sys
import os
import shutil

def createTempFolder(tempFolderName):
        shutil.rmtree(tempFolderName)
        os.mkdir(tempFolderName)

def downloadVideo(url, tempFolderName):
    yt = YouTube(url)
    filename = yt.filename
    yt.set_filename('tempVideo')
    yt.videos[0].download(tempFolderName)
    return {'filename' : filename, 'extension' : yt.videos[0].extension}

def videoToMp3(tempFolderName, extension, filename):
        clip = mp.VideoFileClip(tempFolderName + "tempVideo." + extension)
        clip.audio.write_audiofile("exported/" + filename  + ".mp3")

def main():
        tempFolderName = 'temp/'
        if sys.argv[1]:
                createTempFolder(tempFolderName)
                videoResult = downloadVideo(sys.argv[1], tempFolderName)
                videoToMp3(tempFolderName, videoResult['extension'], videoResult['filename'])
                shutil.rmtree(tempFolderName)
        else:
                print ("Please enter a youtube url as argument")

main()
