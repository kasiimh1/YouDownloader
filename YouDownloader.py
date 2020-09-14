from __future__ import unicode_literals
import youtube_dl, sys, argparse, platform, os

links = []
ytoptions = []

def downloader(link, ytoptions):
    for index, x in enumerate(link):
        with youtube_dl.YoutubeDL(ytoptions) as ydl:
            ydl.download([x])
            print("DOWNLOAD FINISHED!")
        print("Successfully Downloaded", index + 1 , "/", len(link) , "items")
    return

parser = argparse.ArgumentParser(description='YouDownloader: Easy to use Youtube Downloader Tool by Kasiimh1')
parser.add_argument('-a', help='Download Audio Only', action='store_true')
parser.add_argument('-c', help='Set Codec When Downloading Audio Only') 
parser.add_argument('-e', help='Exit Program', action='store_true')
parser.add_argument('-i', help='Install dependancies', action='store_true')
parser.add_argument('-l', help='Video Links You Wish To Download In This Format -> link,link,link')
parser.add_argument('-v', help='Download Video in Highest Quality Available', action='store_true')
parser.add_argument('-s', help='Fetch Subtitles for Videos Only', action='store_true') 
args = parser.parse_args()

parser.print_help()

if args.e:
    sys.exit(-1)

if args.c:
    audioCodec = args.c
else:
    audioCodec = 'mp3'

if args.i:
    print("Install Dependencies")
    print("[Windows] choco install ffmpeg (copy into admin cmd window)")
    print("[macOS] brew install ffmpeg && brew install libmagic")

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
    if args.s:
        ytoptions = {'quiet': 'opts.quiet',
            'no_warnings': 'opts.no_warnings',
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s',
            'merge_output_format': 'mkv',
            'writesubtitles' : True }
            # 'embedsubtitles' : True }
    else:
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