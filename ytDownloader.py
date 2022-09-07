from pytube import YouTube
import sys

link = sys.argv[1]

if len(sys.argv) != 2:
    print("Usage: python3 ytDownloader.py LINK")

yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download("./videos")
