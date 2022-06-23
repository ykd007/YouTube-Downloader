# import imp
from multiprocessing.connection import wait
import os
from pytube import Playlist, YouTube
import time
import shutil

 

def downloadplaylist():
    link = input("\tEnter link: ")
    try :
        count = 0
        p = Playlist(link)
        print("\n\tFetching Details ...")
        print("\t-----------------------------------\n")
        
        # making a new folder with the title name
        directory = p.title
        parent_dir = "/home/teladmin/Desktop/Practice/Youtube Downloader"
        path = os.path.join(parent_dir, directory)
        if(os.path.exists(path)):
            shutil.rmtree(path)
        os.mkdir(path)
        print("\tVideo Title : ", p.title)
        ch = input("\tDo you wish to continue(y/n)? : ")
        if(ch == 'y'):
            for url in p.video_urls:
                count = count+1
                vid = YouTube(url)
                vid = vid.streams.get_highest_resolution()
                print("Downloading .. ", count," : ",  YouTube(url).title)
                vid.download(path)
                print("\tDownload Complete !\n")
        else:
            return 0

    except:
        print("\n\nAn Error occured while connecting whith YouTube Servers", end="")
        for i in range (0, 5):
            time.sleep(1)
            print(". ", end="")

def download():
    link = input("\tEnter link: ")
    try:
        vid = YouTube(link)
        print("\tVideo Title : ", vid.title)
        ch = input("\tDo you wish to continue(y/n)? : ")
        if(ch == 'y'):
            vid = vid.streams.get_highest_resolution()
            print("\tDownloading ", vid.title)
            vid.download("/home/teladmin/Desktop/Practice/Youtube Downloader")
            print("\tDownload Complete !")
            return 0
        else:
            return 0

    except:
        print("\n\nAn Error occured while connecting whith YouTube Servers", end="")
        for i in range (0, 3):
            time.sleep(1)
            print(". ", end="")

# driver code:
while(True):
    choice = int(input('''\n\n
    🆈 🆃     🅳 🅾 🆆 🅽 🅻 🅾 🅰 🅳 🅴 🆁
        1. Download playlist
        2. Download single video
        0. Exit\n
    Enter an option: '''))

    if choice == 1:
        downloadplaylist()
    elif choice == 2:
        download()
    elif choice == 0:
        print('\nThanks for using our services\n')
        exit()
    else:
        print('\tInvalid choice')
    