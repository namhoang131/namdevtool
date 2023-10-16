import requests
from bs4 import BeautifulSoup
from colored import fg, attr
from datetime import date
from datetime import datetime
from os.path import isfile
from time import sleep,strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import os, sys
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
System.Title("URL LINK GOOGLE")
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
            \033[1;31m    TOOL GET URL LINK TỪ GOOGLE
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯ """)
print(f"{attr('bold')}{fg(226)}Nhập từ khóa tìm kiếm: {attr('reset')}", end="")
search_term = input()

print(f"{attr('bold')}{fg(226)}Nhập số lượng kết quả cần tìm: {attr('reset')}", end="")
num_results = int(input())

url = f"https://www.google.com/search?q={search_term}&num={num_results}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

file_name = "links.txt"
with open(file_name, "w") as file:
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if href.startswith("/url?q="):
            link_text = href[7:]
            print(f"{fg(75)}{link_text}{attr('reset')}")
            file.write(link_text + "\n")

print(f"Lưu các liên kết vào file {file_name}")
print(f"Made By Nam Dev")