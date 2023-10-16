from pytube import YouTube
import threading,base64
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
import requests
import socket
import os, sys
System.Clear()
System.Title("Tải Video Trên YTB")
System.Size(140, 40)
#màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
lam = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
load = (f"{luc}Vui Lòng Đợi Tool Chạy!!\n")
made = (f"{lam}Tool Made By Nam")
System.Title("Download Video Trên YTB")
for x in load:
    sys.stdout.write(x)
    sys.stdout.flush()
    sleep(0.100)
for x in made:
    sys.stdout.write(x)
    sys.stdout.flush()
    sleep(0.120)
print(f"""
            \033[1;36m╭─⋞─────────────────────────────────────────────────────╮
            \033[1;31m███╗   ██╗ █████╗ ███╗   ███╗    ██████  ███████╗██╗   ██╗          
            \033[1;32m████╗  ██║██╔══██╗████╗ ████║    ██╔══██╗██╔════╝██║   ██║          
            \033[1;33m██╔██╗ ██║███████║██╔████╔██║    ██║  ██║█████╗  ╚██╗ ██╔╝          
            \033[1;34m██║╚██╗██║██╔══██║██║╚██╔╝██║    ██║  ██║██╔══╝   ╚████╔╝           
            \033[1;35m██║ ╚████║██║  ██║██║ ╚═╝ ██║    ██████╔╝███████╗  ╚██╔╝            
            \033[1;36m╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   
            \033[1;34m Youtube : \033[1;37mhttps://youtube.com/@NamTool1
            \033[1;34m Nhóm Zalo : \033[1;37mhttps://zalo.me/g/kfmgqm225
            \033[1;34m Facebook   : \033[1;37mhttps://facebook.com/nam.nhn131 
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯ 
            \033[1;31m    TOOL TẢI VIDEO TỪ YOUTUBE
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯ """)
def download_video(url, NamVN):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=NamTool)
        print("Video đã được tải xuống thành công!")
    except Exception as e:
        print("Đã xảy ra lỗi:", str(e))
video_url = input(f"{trang}Nhập link video youtube cần tải:{vang}")
NamTool = "videoyt"
print("Tool by NamDev")
download_video(video_url, NamTool)