
from __future__ import unicode_literals

import bs4
import requests
import os
import sys
import youtube_dl

print "Enter the name of the song: "
song = raw_input()
print "Keep waiting. Your gaana is downloading."
print "Downloading " + song

if not os.path.exists("Script_Download_Music"):
	os.makedirs("Script_Download_Music")

url = "https://www.youtube.com/results?search_query=" + song

r = requests.get(url)
r.raise_for_status()

s = bs4.BeautifulSoup(r.text)

text = s.select("h3 a")

title = text[0].get("title")
print "Downloading : " + title

url =  "https://www.youtube.com" + text[0].get("href")

os.chdir("Script_Download_Music")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print "Your song has been downloaded. Check the Script_Donwload_Music folder for the song."