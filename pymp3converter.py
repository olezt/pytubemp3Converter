import moviepy.editor as mp
from pytube import YouTube
import sys

if sys.argv[1]:
    yt = YouTube(sys.argv[1])
    filename = yt.filename
    extension = yt.videos[0].extension
    yt.set_filename('tempVideo')
    yt.videos[0].download('temp/')
    clip = mp.VideoFileClip("temp/tempVideo." + extension)
    clip.audio.write_audiofile("exported/" + filename + ".mp3")
else:
    print ("Please enter a youtube url as argument")

