from __future__ import unicode_literals
import youtube_dl
import sys, argparse, platform, os

def installDep():
    if platform.system() == "Darwin":
        os.system("brew install libmagic && brew install ffmpeg")
    if platform.system() == "Windows":
        os.system("choco install ffmpeg")
    if platform.system() == None:
        print("Cannot Determine OS")

links = []
ytoptions = []

def downloader(link, ytoptions):
    for index, x in enumerate(link):
        with youtube_dl.YoutubeDL(ytoptions) as ydl:
            ydl.download([x])
            print("DOWNLOAD FINISHED!")
        print("Successfully Downloaded", index + 1 , "/", len(link) , "items")
    return

parser = argparse.ArgumentParser(description='YouDownloader: Easy to use Youtube Tool by Kasiimh1')
parser.add_argument('-a', help='Download Audio Only', action='store_true')
parser.add_argument('-c', help='Set Codec When Downloading Audio Only') 
parser.add_argument('-e', help='Exit Program', action='store_true')
parser.add_argument('-i', help='Install dependancies', action='store_true')
parser.add_argument('-l', help='Video Links You Wish To Download In This Format -> link,link,link')
parser.add_argument('-v', help='Download Video in Highest Quality Available', action='store_true')
args = parser.parse_args()

parser.print_help()

if args.e:
    sys.exit(-1)

if args.c:
    audioCodec = args.c
else:
    audioCodec = 'mp3'

if args.i:
    print("Installing Dependencies")
    installDep()

if args.a:
    ytoptions = {'quiet': 'opts.quiet',
                'no_warnings': 'opts.no_warnings',
                'format': 'bestaudio/best',
                'outtmpl':'%(title)s.%(ext)s',
                'postprocessors': [{
                                    'key': 'FFmpegExtractAudio',
                                    'preferredcodec': audioCodec,
                                    'preferredquality': '320'}]}

if args.v:
    ytoptions = {'quiet': 'opts.quiet',
        'no_warnings': 'opts.no_warnings',
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s',
        'merge_output_format': 'mkv'}

if args.v and args.l:
    links = args.l.split(',')
    downloader(links, ytoptions)

if args.a and args.l:
    links = args.l.split(',')
    downloader(links, ytoptions)
