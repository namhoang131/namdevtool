import requests
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import time
from time import sleep
import pystyle
import random


import time

def slow_type(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def banner():
    slow_type("""

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
            \033[1;31m    TOOL LỌC PROXY V1
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯\n

                                   
""", delay=0.00)



def clear():
    os.system("cls" if os.name == "nt" else "clear")


def thanh():
    print("\033[1;36m———————————————————————-—————————————————————————————————————————————-——————————————————————————————————")



# Bắt đầu chay tool
sleep(3)
clear()
banner()
thanh()
slow_type(" ")
sleep(3)
proxy_list = input("\033[1;37m Vui lòng nhập file chứa Proxy: \033[1;33m")
with open(proxy_list, 'r') as file:
    proxy_list = file.read().split("\n")
    proxy_count = len(proxy_list)
luu = input("\033[1;37m Vui lòng nhập tệp để lưu Proxy Live: \033[1;33m")
slow_type(f" \033[1;36mTìm Thấy \033[1;33m{proxy_count} \033[1;36m Trong File Của Bạn")
sleep(2)
slow_type(" \033[1;31mVui Lòng Đợi Vài Giây")
sleep(3)
print(" \033[1;32m Bắt Đầu Chạy Tool")
print("\033[1;37m ———————————————————————————————————————————————")
sleep(3)
list = []
for p in proxy_list:
    prx = p.strip("\n")
    list.append(prx)


def check_proxy(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    
    try:
        response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=20)
        if response.status_code == 200 or response.status_code == 202 or response.status_code == 504 or response.status_code == 503 or response.status_code == 502 or response.status_code == 500:
            detect_location(proxy)
            open(luu,'a').write(proxy+'\n')
            return True
    except requests.exceptions.RequestException:
        pass

    print(f" \033[1;37m[\033[1;31m+\033[1;37m] \033[1;37m{proxy} \033[1;31m• \033[1;37mUnknown/Unknown \033[1;31m• \033[1;31mBAD")
    return False


def detect_location(proxy):
    ip_address = proxy.split(':')[0]
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "success":
            print(f" \033[1;37m[\033[1;31m+\033[1;37m] \033[1;37m{proxy} \033[1;31m• \033[1;37m{data['country']}/{data['city']} \033[1;31m• \033[1;32mLIVE")
            open(luu,'a').write(proxy+'\n')
        else:
            print(" \033[1;37m[\033[1;31m+\033[1;37m] \033[1;31mFailed to detect location for proxy.")


def process_proxy(proxy):
    if check_proxy(proxy):
        pass


num_workers = 200

with ThreadPoolExecutor(max_workers=num_workers) as executor:
    executor.map(process_proxy, proxy_list)

print(
    f" \033[1;32mQuá Trình Hoàn Tất. Hiện Có Trong \033[1;37m{luu} \033[1;32mCó \033[1;37m%s \033[1;32mProxies Live"
    % (len(open(f"{luu}").readlines()))
)
logout = input(" Ấn enter để thoát!")
exit()