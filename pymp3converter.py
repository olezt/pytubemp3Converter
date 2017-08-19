import moviepy.editor as mp
from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=lVIUnuDby7U")
filename = yt.filename
extension = yt.videos[0].extension
yt.set_filename('tempVideo')
yt.videos[0].download('temp/')
clip = mp.VideoFileClip("temp/tempVideo." + extension)
clip.audio.write_audiofile("exported/" + filename + ".mp3")
