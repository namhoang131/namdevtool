import socket
import requests
import concurrent.futures
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
import requests
import socket
import os, sys
trang = "\033[1;37m"
luc = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lam = "\033[1;36m"
System.Title("Lọc Proxy")
print("""
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
            \033[1;31m    TOOL LỌC PROXY V2
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯\n""")
def check_proxy(proxy):
    try:
        socket.setdefaulttimeout(10)
        host, port = proxy.split(':')
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, int(port)))
        return True
    except:
        pass
    return False

def remove_dead_proxies(input_file):
    with open(input_file, 'r') as file:
        proxies = file.readlines()

    alive_proxies = []
    proxy_count = len(proxies)  # Số lượng proxy trong danh sách ban đầu
    live_proxy_count = 0  # Số lượng proxy sống đã quét ra
    die_proxy_count = 0  # Số lượng proxy die đã quét ra và bị loại bỏ

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for proxy in proxies:
            future = executor.submit(check_proxy, proxy.strip())
            futures.append((proxy.strip(), future))

        for proxy, future in futures:
            if future.result():
                alive_proxies.append(proxy)
                live_proxy_count += 1
                print(f'{luc}| CHECK PROXY | Nam~Tool:{proxy} Trạng thái: Live')
            else:
                print(f'{do}| CHECK PROXY | Nam~Tool:{proxy} Trạng thái: Die')
                if remove_proxy(proxy):
                    print(f'{luc}| REMOVE PROXY | Nam~Tool:{proxy} Trạng thái: Xóa thành công')
                    die_proxy_count += 1
                else:
                    print(f'{do}| REMOVE PROXY | Nam~Tool:{proxy} Trạng thái: Xóa không thành công')

    with open(input_file, 'w') as file:
        file.write('\n'.join(alive_proxies))

    print(f'\nCheck thành công {proxy_count} proxy')
    print(f'Proxy Live: {live_proxy_count}')
    print(f'Proxy Die: {die_proxy_count}')
    print(f'Tool Made By Nam Tool !')

def remove_proxy(proxy):
    try:
        with open(input_file, 'r') as file:
            proxies = file.readlines()

        with open(input_file, 'w') as file:
            for line in proxies:
                if line.strip() != proxy:
                    file.write(line)

        return True
    except:
        return False

# Đường dẫn tới tệp chứa danh sách proxy
input_file = input(f"{do}[{vang}</>{do}]{trang}Nhập file proxy: {vang}")

# Kiểm tra và xóa proxy không hoạt động, chỉ xóa proxy die khỏi danh sách ban đầu
remove_dead_proxies(input_file)