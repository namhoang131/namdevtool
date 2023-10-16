import requests
from requests import Session
import random
from colorama import init, Fore
import os, sys
from os.path import isfile
from time import sleep,strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from datetime import datetime
System.Clear()
System.Title("HENTAI")
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
    System.Clear()
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
            \033[1;31m               TOOL DOWNLOAD ẢNH HENTAI
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯ """)
class Haiten():
    def __init__(self):
        self.session = requests.Session()
    
    def generator(self):
        init(autoreset=True) # Khởi tạo colorama
    
        self.url = 'https://api.waifu.pics/nsfw/waifu'
        
        while True:
            try:
                self.get_pic = requests.get(self.url).json()
                self.url_pic = self.get_pic["url"]
                break
            except Exception as e:
                print(Fore.RED + str(e)) # In lỗi với màu đỏ
                continue
        
        def random_id(length):
            self.number = '0123456789'
            self.alpha = 'abcdefghijklmnopqrstuvwxyz'
            self.id = ''
            for i in range(0,length,2):
                self.id += random.choice(self.number)
                self.id += random.choice(self.alpha)
            return self.id
        
        self.rd = random_id(5)
        
        while True:
            try:
                self.picture = self.session.get(self.url_pic)
                with open(f'{self.rd}.png', 'wb') as f:
                    f.write(self.picture.content)
                break
            except Exception as e:
                print(Fore.RED + str(e)) # In lỗi với màu đỏ
                continue
        
h = Haiten()

while True:
    num_downloads = 20  

    for _ in range(num_downloads):
        h.generator()
        print(Fore.GREEN + "[Nam~Tool] Mỗi Lần Tải 20 Ảnh Nha!!!") # In thông báo với màu xanh lá cây
    
    print(Fore.YELLOW + "Bạn muốn tiếp tục tải ảnh không? (Y/N)") # In câu hỏi với màu vàng
    choice = input()
    if choice.lower() == 'n':
        break