import requests,re
import os,sys
import time
import concurrent.futures
from requests import session
from colorama import Fore, Style
from pystyle import Write, Colors
from threading import Thread, Lock
import threading
from random import randint 
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from pystyle import *
trang = '\033[1;37m'
vang = '\033[1;33m'
def genproxy():
    def check(url_gen, luu_live):
        get_proxy = requests.get(url_gen).text
        xoa_line = get_proxy.splitlines()
        for proxy in xoa_line:
            print(proxy)
            with open(luu_live, "a+") as f:
                f.write(proxy + "\n")
    def something():
        System.Clear()
        logo ="""
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
            \033[1;31m                 TOOL GEN PROXY V1
            \033[1;36m╰─────────────────────────────────────────────────────⋟─╯
"""
        print(logo)
    something()
    something()
    luu_live = input(f"{trang}Nhập File Lưu Proxy: {vang}")
    for i in range(3):
        url_gen = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
        check(url_gen, luu_live)
genproxy()