from __future__ import unicode_literals
import youtube_dl

#need to install ffmpeg for this to work

print(" ************************************************\n",
      "Welcome to YouDownloader\n",
      "Created By Kasiimh1\n\n",
      "0 = Exit Program\n",
      "1 = Download Audio Only\n",
      "2 = Download Video in Highest Quality Available\n",
      "************************************************")

print("Enter Option?... ")
option = input()

if (option == '0') is True:
    print("Exiting Program!")
    exit()

else:
    print("Starting download....")
    print("\nEnter links seperate by a comma e.g. link,link,link")
    links = input().split(',')
    
    if (option == '1') is True:
        
        ydl_opts = {'quiet': 'opts.quiet',
            'outtmpl': '%(title)s.%(ext)s',
            'no_warnings': 'opts.no_warnings',
                'format': 'bestaudio/best',
                    'postprocessors': [{
                                       'key': 'FFmpegExtractAudio',
                                       'preferredcodec': 'mp3',
                                       'preferredquality': '320',
                                       }]}

if (option == '2') is True:
    
    ydl_opts = {'quiet': 'opts.quiet',
        'no_warnings': 'opts.no_warnings',
            'format': 'bestvideo+bestaudio/best',
                'outtmpl': '%(title)s',
                    'merge_output_format': 'mkv'
                }

for index, x in enumerate(links):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([x])
        print("DOWNLOAD FINISHED!")
        print("Successfully Downloaded", index + 1 , "/", len(links) , "items")        
