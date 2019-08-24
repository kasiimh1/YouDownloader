from __future__ import unicode_literals
import youtube_dl
import sys

#**** need to install ffmpeg for this to work ****#

links = []
ytoptions = []

def printHelp():
    print("\nWelcome to YouDownloader\nCreated By Kasiimh1\n\n",
            "-e, -exit    Exit Program\n",
            "-h, -help    Show Help Screen\n",
            "-l, -link    Video Links You Wish To Download In This Format -> link,link,link\n",
            "-a, -audio   Download Audio Only\n",
            "-v, -video   Download Video in Highest Quality Available\n")
    return

def downloader(link, ytoptions):
    for index, x in enumerate(link):
        with youtube_dl.YoutubeDL(ytoptions) as ydl:
            ydl.download([x])
            print("DOWNLOAD FINISHED!")
        print("Successfully Downloaded", index + 1 , "/", len(link) , "items")
    return

def exit():
    sys.exit()
    return

if (len(sys.argv) == 1):
    printHelp()
    exit()

if len(sys.argv) >= 2:
    
    #exit program
    if (sys.argv[1] == '-e' or sys.argv[1] == '-exit'):
        print("Exiting Program!")
        exit()

    if (sys.argv[1] == '-help' or sys.argv[1] == '-h'):
        printHelp()
        exit()

    if (sys.argv[1] == '-a' or sys.argv[1] == '-audio'):
        ytoptions = {'quiet': 'opts.quiet',
                        'no_warnings': 'opts.no_warnings',
                        'format': 'bestaudio/best',
                        'outtmpl': '%(title)s',
                        'postprocessors': [{'key': 'FFmpegExtractAudio',
                                            'preferredcodec': 'mp3',
                                            'preferredquality': '320'}]}

    if (sys.argv[1] == '-v' or sys.argv[1] == '-video'):
        ytoptions = {'quiet': 'opts.quiet',
                        'no_warnings': 'opts.no_warnings',
                        'format': 'bestvideo+bestaudio/best',
                        'outtmpl': '%(title)s',
                        'merge_output_format': 'mkv'}

    if (sys.argv[1] == '-v' or sys.argv[1] == '-video' and sys.argv[2] == '-l' or sys.argv[2] == '-link'):
        links = sys.argv[3].split(',')
        downloader(links, ytoptions)
        exit()

    if (sys.argv[1] == '-a' or sys.argv[1] == '-audio' and sys.argv[2] == '-l' or sys.argv[2] == '-link'):
        links = sys.argv[3].split(',')
        downloader(links, ytoptions)
        exit()
