import youtube_dl
import os

os.system("cls")

url_file = str(input("Enter YouTube Url: "))
try:
    ydl_opts = {'outtmpl': 'c:/Video_Downloader/%(title)s.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'{url_file}'])
except Exception as e:
    print("Error Occured", format(e))