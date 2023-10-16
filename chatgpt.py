from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import socket
from pystyle import *
#màu
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
#Đánh Dấu Bản Quyền
HĐ_tool = trang + " " + trang + "[" + do + "+_+" + trang + "] " + trang + "=> "
hdang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"
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
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S%p")
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os

os.system('clear')
banner = f'''
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
            \033[1;31m                     TOOL CHAT GPT
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
'''
print(f"{trang} ➩ Ngày{trang} : {do}{ngay_hom_nay}{vang} |{luc} Tháng{trang}: {do}{thang_nay} {vang}| {luc}Năm{trang}: {do}{nam_}{vang} | {luc}Thời Gian: {do}{time}")
print(f'{trang} ➩ IP Hiện Tại Của Bạn : {vang}{ip}')
print(banner)
def gpt():
  while True:
    tin_nhan = input(" \033[1;91m[\033[1;33m</>\033[1;91m] => \033[1;37mNhập Nội Dung: \033[1;33m")
    cookies = {
        '_ga': 'GA1.1.1363846780.1683999003',
        '_ga_Z6X4XPL08Y': 'GS1.1.1683999002.1.1.1683999003.0.0.0',
        '__gads': 'ID=73d3320f403315ab-228ebcf9b3e000af:T=1683999003:RT=1683999003:S=ALNI_MYjiDyFTVXe4i-Ul91vim1Z2Uzozw',
        '__gpi': 'UID=00000c05958a891e:T=1683999003:RT=1683999003:S=ALNI_MZrRRQMBseV2bblhmUaaeOVW0KDxA',
        'XSRF-TOKEN': 'eyJpdiI6Ilo2UWsrWlBNSFNTRHVOK0Fqb1E0VFE9PSIsInZhbHVlIjoiT2xzazRmOTh4YitRa05IUDM1dWppYVRPN1BVU3NGRjB5MHVlb2Z1YzRjZ0xXZzNYN0d3cDl5N3ZRbjkwWDk2dUVOYWZlWGltam1ZMTNDaVdNUmFxSm1tOXoyNnhpZ1dXVGluQXY2aDZBMHFrVlZjSzM4Tk9nN3k5QXp6UDV0dGoiLCJtYWMiOiJmOGZjYTc5MGIzMjNkZDk5ZGZhZjY2NDBiNmU1YzI5NjIxNzIzODg3YmMyY2YzODI3NzRkYzFjOTNjNDVlM2Y3In0%3D',
        'chatgptorg_session': 'eyJpdiI6Ik51aHR4NlhZRVNIdmVFV2VFdk53VlE9PSIsInZhbHVlIjoiODZMOTZFVzFRSFpTaXFqd1luT3pBbzNJM1kzaWwzTG5rWDNPNkZBVzVmRExtUm1qT1hqbTZxNCtXTWdUN2lHcUd6bSt5NWFBWFFCMjJSZmpUbVZOd3VzT2V0Z3Y5blhtRUlJV2llL0RuUnUzM3lFWFlBakxPVVJNVXJwMTlDUHEiLCJtYWMiOiJlYThhMTY1MzNjOTYwYmE3ODU4ZjY0YjNiZDQxMzQyOWU0YTM0MjI2ZGRiNTk3MGIxODRlZmJhNDk2ZWQ3OTdjIn0%3D',
  }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': '_ga=GA1.1.1363846780.1683999003; _ga_Z6X4XPL08Y=GS1.1.1683999002.1.1.1683999003.0.0.0; __gads=ID=73d3320f403315ab-228ebcf9b3e000af:T=1683999003:RT=1683999003:S=ALNI_MYjiDyFTVXe4i-Ul91vim1Z2Uzozw; __gpi=UID=00000c05958a891e:T=1683999003:RT=1683999003:S=ALNI_MZrRRQMBseV2bblhmUaaeOVW0KDxA; XSRF-TOKEN=eyJpdiI6Ilo2UWsrWlBNSFNTRHVOK0Fqb1E0VFE9PSIsInZhbHVlIjoiT2xzazRmOTh4YitRa05IUDM1dWppYVRPN1BVU3NGRjB5MHVlb2Z1YzRjZ0xXZzNYN0d3cDl5N3ZRbjkwWDk2dUVOYWZlWGltam1ZMTNDaVdNUmFxSm1tOXoyNnhpZ1dXVGluQXY2aDZBMHFrVlZjSzM4Tk9nN3k5QXp6UDV0dGoiLCJtYWMiOiJmOGZjYTc5MGIzMjNkZDk5ZGZhZjY2NDBiNmU1YzI5NjIxNzIzODg3YmMyY2YzODI3NzRkYzFjOTNjNDVlM2Y3In0%3D; chatgptorg_session=eyJpdiI6Ik51aHR4NlhZRVNIdmVFV2VFdk53VlE9PSIsInZhbHVlIjoiODZMOTZFVzFRSFpTaXFqd1luT3pBbzNJM1kzaWwzTG5rWDNPNkZBVzVmRExtUm1qT1hqbTZxNCtXTWdUN2lHcUd6bSt5NWFBWFFCMjJSZmpUbVZOd3VzT2V0Z3Y5blhtRUlJV2llL0RuUnUzM3lFWFlBakxPVVJNVXJwMTlDUHEiLCJtYWMiOiJlYThhMTY1MzNjOTYwYmE3ODU4ZjY0YjNiZDQxMzQyOWU0YTM0MjI2ZGRiNTk3MGIxODRlZmJhNDk2ZWQ3OTdjIn0%3D',
        'Origin': 'https://chatgpt.org',
        'Referer': 'https://chatgpt.org/chat',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
  }

    json_data = {
        'message': tin_nhan,
        'temperature': 1,
        'presence_penalty': 0,
        'top_p': 1,
        'frequency_penalty': 0,
  }

    response = requests.post('https://chatgpt.org/api/text', cookies=cookies, headers=headers, json=json_data).json()
    rp = response['message']
    print(" \033[1;91m[\033[1;33m</>\033[1;91m] => \033[1;37mTrả Lời: \033[1;33m",rp)

gpt()