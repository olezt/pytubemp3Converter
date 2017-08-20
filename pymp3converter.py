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

def downloadVideo(url, tempFolderName, filenamePrefix, videoQuality):
    print (videoQuality)
    yt = YouTube(url)
    filename = yt.filename
    yt.set_filename(filenamePrefix + 'tempVideo')
    yt.videos[videoQuality].download(tempFolderName)
    return {'filename' : filename, 'extension' : yt.videos[videoQuality].extension}

def videoToMp3(tempFolderName, extension, filename, filenamePrefix):
    id = id_generator()
    clip = mp.VideoFileClip(tempFolderName + filenamePrefix + "tempVideo." + extension)
    clip.audio.write_audiofile("exported/" + filename + " " + id  + ".mp3")

def downloadAndConvert(url, tempFolderName, filenamePrefix, videoQuality):
    videoResult = downloadVideo(url, tempFolderName, filenamePrefix, videoQuality)
    videoToMp3(tempFolderName, videoResult['extension'], videoResult['filename'], filenamePrefix)

def readFile(filename):
    return tuple(open(filename, 'r'))

def main():
    avArgvs = ['-u', '-f']
    tempFolderName = 'temp/'
    deleteTempFolder(tempFolderName)
    createNewTempFolder(tempFolderName)
    videoQuality = 0 if (len(sys.argv)>3 and sys.argv[3]=='-lq') else -1
    if len(sys.argv)>=3 and sys.argv[1]=='-u':
        url = sys.argv[2]
        downloadAndConvert(url, tempFolderName, '', videoQuality)
    elif len(sys.argv)>=3 and sys.argv[1]=='-f':
        filename = sys.argv[2]
        urls = readFile(filename)
        filenamePrefix = 0 
        for url in urls:
            filenamePrefix += 1
            downloadAndConvert(url, tempFolderName, str(filenamePrefix), videoQuality)
    else:
        print ("Please use one of the available arguments: " + str(avArgvs))
    deleteTempFolder(tempFolderName)

main()
