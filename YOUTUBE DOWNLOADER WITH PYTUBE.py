from pytube import YouTube


url = "https://www.youtube.com/watch?v=ZTrrc6Ni5eM"

try:
   video = YouTube(url)
   video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
   print("The video is downloaded in MP4")
except KeyError:
   print("Unable to fetch video information. Please check the video URL or your network connection.")
