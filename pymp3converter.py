import moviepy.editor as mp
from pytube import YouTube
import sys, os, shutil, string, random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """create a random id"""
    return ''.join(random.choice(chars) for _ in range(size))

def deleteTempFolder(tempFolderName):
    """delete the temp folder where videos are downloaded"""
    try:
        shutil.rmtree(tempFolderName)
    except:
        pass

def createNewTempFolder(tempFolderName):
    """create the temp folder where videos are downloaded"""
    deleteTempFolder(tempFolderName)
    os.mkdir(tempFolderName)

def downloadVideo(url, tempFolderName, filenamePrefix, videoQuality):
    """download a given video"""
    print (videoQuality)
    yt = YouTube(url)
    filename = yt.filename
    yt.set_filename(filenamePrefix + 'tempVideo')
    yt.videos[videoQuality].download(tempFolderName)
    return {'filename' : filename, 'extension' : yt.videos[videoQuality].extension}

def videoToMp3(tempFolderName, extension, filename, filenamePrefix):
    """convert a given video to mp3"""
    id = id_generator()
    clip = mp.VideoFileClip(tempFolderName + filenamePrefix + "tempVideo." + extension)
    clip.audio.write_audiofile("exported/" + filename + " " + id  + ".mp3")

def downloadAndConvert(url, tempFolderName, filenamePrefix, videoQuality):
    """download and convert to mp3 a given video"""
    videoResult = downloadVideo(url, tempFolderName, filenamePrefix, videoQuality)
    videoToMp3(tempFolderName, videoResult['extension'], videoResult['filename'], filenamePrefix)

def readFile(filename):
    """read line by line a given file"""
    return tuple(open(filename, 'r'))

def main():
    """main functionality"""
    avArgvs = ['-u', '-f']
    tempFolderName = 'temp/'
    deleteTempFolder(tempFolderName)
    createNewTempFolder(tempFolderName)
    videoQuality = 0 if (len(sys.argv)>3 and sys.argv[3]=='-lq') else -1
    #download/convert specific video, use of -u cli argument
    if len(sys.argv)>=3 and sys.argv[1]=='-u':
        url = sys.argv[2]
        downloadAndConvert(url, tempFolderName, '', videoQuality)
    #download/convert list of videos, use of -f cli argument
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
